# 登陆接口
curl --request POST --url https://121.199.7.231:18443/daneng/get_token_by_barcode --header 'X-Partner-ID: DANENGVXCLOUDS' --header 'content-type: application/json' --header 'sign: 36d2f1821580475a' --header 'time: 1602239080476' --data '{
"barcode":"15001412010963"
}'
# 列表接口
curl --request POST --url https://121.199.7.231:18443/daneng/get_list_results --header 'X-Token: A226BDEBC9884121BFBDF6CD9B344A87' --header 'content-type: application/json' --data '{
"barcode":"DN202205050064"
}'
# 详情接口
curl --request POST --url https://121.199.7.231:18443/daneng/get_case_detail_result --header 'X-Token: A226BDEBC9884121BFBDF6CD9B344A87' --header 'content-type: application/json' --data '{
"barcode": "DN202205050064",
"case": "Vitamin D"
}'