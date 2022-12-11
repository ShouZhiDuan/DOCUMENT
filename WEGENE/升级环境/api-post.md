# 1、登陆接口
```shell
curl --location --request POST 'https://nvxclouds-private-computing.wegene-io.com/daneng/get_token_by_barcode' \
--header 'X-Partner-ID: DANENGVXCLOUDS' \
--header 'time: 1602239080476' \
--header 'sign: 2f4f7c2020de6052' \
--header 'Content-Type: application/json' \
--data-raw '{
"barcode":"20091811472139"
}'
```
```json
{
    "expire_time": 1670733888837,
    "token": "97A204970E464FF6B1F59DD22E01AA56"
}
```
# 2、列表接口
```shell
curl --location --request POST 'https://nvxclouds-private-computing.wegene-io.com/daneng/get_list_results' \
--header 'X-Token: 97A204970E464FF6B1F59DD22E01AA56' \
--header 'Content-Type: application/json' \
--data-raw '{
    "barcode":"D2111186500001"
}'
```
```json
[
    {
        "result": "高",
        "case": "Vitamin B2"
    },
    {
        "result": "正常",
        "case": "Vitamin B6"
    },
    {
        "result": "高",
        "case": "Iron"
    },
    {
        "result": "高",
        "case": "Folic Acid"
    },
    {
        "result": "稍高",
        "case": "Vitamin C"
    },
    {
        "result": "正常",
        "case": "Vitamin E"
    },
    {
        "result": "正常",
        "case": "Vitamin D"
    },
    {
        "result": "高",
        "case": "Zinc"
    },
    {
        "result": "稍高",
        "case": "Calcium"
    },
    {
        "result": "稍高",
        "case": "Vitamin B12"
    }
]
```

# 3、详情接口
```shell
curl --location --request POST 'https://nvxclouds-private-computing.wegene-io.com/daneng/get_case_detail_result' \
--header 'X-Token: 8B91AFB52ED1432B9BFD2C6D4755B169' \
--header 'Content-Type: application/json' \
--data-raw '{
    "barcode":"D2111186500001",
    "case":"Calcium"
}'
```
```json
{
    "result": "success",
    "genotypes": [
        {
            "description": "rs7975232有AA、AC和CC三种基因型，在中国女性人群中的分布是AA 65.4%，AC 28.0%，CC 6.5% [8]。不同基因型钙利用能力为：AA > AC > CC。",
            "rsid": "RS7975232",
            "rsname": "VDR Apa1 rs7975232",
            "genotype": "AC"
        },
        {
            "description": "rs1544410有CC、CT和TT三种基因型，在中国人群中的分布是CC 90.5%，CT 9.5%，TT 0% [4]。不同基因型钙利用能力为：CC > CT > TT。",
            "rsid": "RS1544410",
            "rsname": "VDR Bsm1 rs1544410",
            "genotype": "CC"
        }
    ],
    "case_result": "稍高"
}
```