package com.example.sportmusic_1;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import java.time.Instant;

//主页
public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    //初始化fragment
    private HomePageFragment mHomePageFragment;
    private MatchPageFragment mMatchPageFragment;
    private RecommendPageFragment mRecommendPageFragment;
    private MinePageFragment mMinePageFragment;

    //片段类容
    private FrameLayout mFlFragmentContent;
    //底部4个按钮
    private RelativeLayout mRlFirstLayout;
    private RelativeLayout mRlSecondLayout;
    private RelativeLayout mRlThirdLayout;
    private RelativeLayout mRlFourLayout;

    private ImageView mIvFirstHome;
    private TextView mTvFirstHome;
    private ImageView mIvSecondMatch;
    private TextView mTvSecondMatch;
    private ImageView mIvThirdRecommend;
    private TextView mTvThirdRecommend;
    private ImageView mIvFourMine;
    private TextView mTvFourMine;
    private FragmentManager mFragmentManager;
    private FragmentTransaction mTransaction;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mFragmentManager = getSupportFragmentManager();

        //=============================沉侵式状态栏S================================
        //设置状态栏颜色,必须在setContentView之后使用
        //第一个参数:当前页面;第二个参数:颜色;第三个参数:透明度;
        StatusBarUtil.setColor(this, getResources().getColor(R.color.colorStatusBar), 0);
        //=============================沉侵式状态栏E================================

        initView();     //初始化视图
    }

    //此方法可以让app启动页像微信一样,第一次(启动页运行),第二次(无启动页,直接进入主界面)
//    @Override
//    public void onBackPressed() {
//        //super.onBackPressed();    不要调用父类
//        Intent intent = new Intent(Intent.ACTION_MAIN);     //ACTION_MAIN主活动
//        intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);     //标志活动新任务
//        intent.addCategory(Intent.CATEGORY_HOME);           //类型
//        startActivity(intent);
//    }

    private void initView() {
        mFlFragmentContent = (FrameLayout) findViewById(R.id.fl_fragment_content);
        mRlFirstLayout = (RelativeLayout) findViewById(R.id.rl_first_layout);
        mIvFirstHome = (ImageView) findViewById(R.id.iv_first_home);
        mTvFirstHome = (TextView) findViewById(R.id.tv_first_home);
        mRlSecondLayout = (RelativeLayout) findViewById(R.id.rl_second_layout);
        mIvSecondMatch = (ImageView) findViewById(R.id.iv_second_match);
        mTvSecondMatch = (TextView) findViewById(R.id.tv_second_match);
        mRlThirdLayout = (RelativeLayout) findViewById(R.id.rl_third_layout);
        mIvThirdRecommend = (ImageView) findViewById(R.id.iv_third_recommend);
        mTvThirdRecommend = (TextView) findViewById(R.id.tv_third_recommend);
        mRlFourLayout = (RelativeLayout) findViewById(R.id.rl_four_layout);
        mIvFourMine = (ImageView) findViewById(R.id.iv_four_mine);
        mTvFourMine = (TextView) findViewById(R.id.tv_four_mine);
        //给五个按钮设置监听器
        mRlFirstLayout.setOnClickListener(this);
        mRlSecondLayout.setOnClickListener(this);
        mRlThirdLayout.setOnClickListener(this);
        mRlFourLayout.setOnClickListener(this);
        //默认第一个首页被选中高亮显示
        mRlFirstLayout.setSelected(true);
        mTransaction = mFragmentManager.beginTransaction();
        mTransaction.replace(R.id.fl_fragment_content, new HomePageFragment());
        mTransaction.commit();
    }

    @Override
    public void onClick(View v) {
        mTransaction = mFragmentManager.beginTransaction(); //开启事务
        hideAllFragment(mTransaction);
        switch (v.getId()){
            //首页
            case R.id.rl_first_layout:
                seleted();
                mRlFirstLayout.setSelected(true);
                if (mHomePageFragment == null) {
                    mHomePageFragment = new HomePageFragment();
                    mTransaction.add(R.id.fl_fragment_content,mHomePageFragment);    //通过事务将内容添加到内容页
                }else{
                    mTransaction.show(mHomePageFragment);
                }
                break;
            //赛程
            case R.id.rl_second_layout:
                seleted();
                mRlSecondLayout.setSelected(true);
                if (mMatchPageFragment == null) {
                    mMatchPageFragment = new MatchPageFragment();
                    mTransaction.add(R.id.fl_fragment_content,mMatchPageFragment);    //通过事务将内容添加到内容页
                }else{
                    mTransaction.show(mMatchPageFragment);
                }
                break;
            //推荐
            case R.id.rl_third_layout:
                seleted();
                mRlThirdLayout.setSelected(true);
                if (mRecommendPageFragment == null) {
                    mRecommendPageFragment = new RecommendPageFragment();
                    mTransaction.add(R.id.fl_fragment_content,mRecommendPageFragment);    //通过事务将内容添加到内容页
                }else{
                    mTransaction.show(mRecommendPageFragment);
                }
                break;
            //个人中心
            case R.id.rl_four_layout:
                seleted();
                mRlFourLayout.setSelected(true);
                if (mMinePageFragment == null) {
                    mMinePageFragment = new MinePageFragment();
                    mTransaction.add(R.id.fl_fragment_content,mMinePageFragment);    //通过事务将内容添加到内容页
                }else{
                    mTransaction.show(mMinePageFragment);
                }
                break;
        }
        mTransaction.commit();
    }

    //设置所有按钮都是默认都不选中
    private void seleted() {
        mRlFirstLayout.setSelected(false);
        mRlSecondLayout.setSelected(false);
        mRlThirdLayout.setSelected(false);
        mRlFourLayout.setSelected(false);
    }

    //删除所有fragmtne
    private void hideAllFragment(FragmentTransaction transaction) {
        if (mHomePageFragment != null) {
            transaction.hide(mHomePageFragment);
        }
        if (mMatchPageFragment != null) {
            transaction.hide(mMatchPageFragment);
        }
        if (mRecommendPageFragment != null) {
            transaction.hide(mRecommendPageFragment);
        }
        if (mMinePageFragment != null) {
            transaction.hide(mMinePageFragment);
        }
    }
}
