def tplink_id(b_root, dp ,ds,iptp):
    for i in iptp:
        if i in ds.keys():
           i_c = dp[i][0].index(b_root)
           dp[i][0][i_c] = ds[i]
        else:
           i_c = dp[i][0].index(b_root)
           dp[i][0][i_c] = "11111111"

    return dp
