XHttpConfig().initHttpLogOn(true)
    .initHeaderSetFunc((headers) => {
        headers['model'] = 'xiao mi';
        headers['version'] = '1.0.0';
        headers['platform'] = Platform.OS;
        headers['channelCode'] = 'channelOfficial';
        if (isLogin()) {
            headers['customerId'] = RNStorage.customerId;
            headers['accessToken'] = RNStorage.accessToken;
            headers['refreshToken'] = RNStorage.refreshToken;
        }
    })
    .initParamSetFunc(params => {
        if (isLogin()) {
            params['customerId'] = RNStorage.customerId;
        }
    })
    .initParseDataFunc((result, request, callback) => {
        let {success, json, message, status, response} = result;
        if (status === 503) {// accessToken过期标记
            this.refreshToken(request, callback);
        } else {
            let {data, successful, msg, code} = json;
            callback(success && successful === 1, data || {}, msg || message, code, response);
        }
    });
refreshToken = (request, callback) => {
    if (global.hasQueryToken) {
        global.tokenExpiredList.push({request, callback});
    } else {
        global.hasQueryToken = true;
        global.tokenExpiredList = [{request, callback}];
        const refreshUrl = `${RNStorage.baseUrl}api/refreshToken?refreshToken=${RNStorage.refreshToken}`;
        fetch(refreshUrl).then(resp => {
            resp.json().then(({successful, data: {accessToken}}) => {
                if (successful === 1) {// 获取到新的accessToken
                    RNStorage.accessToken = accessToken;
                    global.tokenExpiredList.map(({request, callback}) => {
                        request.resendRequest(request, callback);
                    });
                    global.tokenExpiredList = [];
                } else {
                    console.log('Token 过期，退出登录');
                }
            });
        }).catch(err => {
            console.log('Token 过期，退出登录');
        }).finally(() => {
            global.hasQueryToken = false;
        });
    }
};
export const RNStorage = {// 持久化数据列表
    customerId: undefined,//客户ID
    accessToken: undefined,//OAuth2.0 accessToken
    refreshToken: undefined,//OAuth2.0 refreshToken
    baseUrl: undefined,
    userInfo: undefined,
    hasLogin: false,
};
import { XHttp } from 'react-native-easy-app';

login = () => {
    let params = {userName: 'zhangsan', userPass: '123456a'};
    XHttp().url('api/login').param(params).formEncoded().get((success, json, message, status, resonse) => {
        if (success) {
            if (resonse.headers && resonse.headers.map) {
                RNStorage.accessToken = resonse.headers.map['x-oss-meta-accesstoken'];
                RNStorage.refreshToken = resonse.headers.map['x-oss-meta-refreshtoken'];
            }
            RNStorage.customerId = json.customerId;
            RNStorage.hasLogin = true;
            this.setState({data: JSON.stringify(json)});
        } else {
            console.log('失败', message);
        }
    });
};
import { XHttp } from 'react-native-easy-app';

queryUserInfo = () => {
    XHttp().url('api/userInfo').formJson().get((success, json, message) => {
        if (success) {
            RNStorage.userInfo = json;
            this.setState({data: JSON.stringify(json)});
        } else {
            console.log('失败', message);
        }
    });
};