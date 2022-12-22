nohup java \
-DQUERY_PROFILE=TEST \
-DTASK_CORN="*/60 * * * * ?" \
-DLOGIN_API=https://beta-nvxclouds-private-computing.wegene-io.com/daneng/get_token_by_barcode \
-DDETAIL_API=https://beta-nvxclouds-private-computing.wegene-io.com/daneng/get_case_detail_result \
-DLIST_API=https://beta-nvxclouds-private-computing.wegene-io.com/daneng/get_list_results \
-DTO_EMAIL=dszazhy1314@163.com \
-jar api-monitor.jar > monitor.log 2>&1 &
