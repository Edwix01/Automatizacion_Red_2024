def tplink_id(b_root, dp ,ds):
    for i in ds.keys():
        i_c = dp[i][0].index(b_root)
        dp[i][0][i_c] = ds[i]
    
    return dp
