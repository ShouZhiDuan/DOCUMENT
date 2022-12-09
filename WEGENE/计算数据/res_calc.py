## 从 WeGene 获取的某个用户的结果
user_input = {
    'RS1801133': 'AG', 
	'RS1801131': 'GT',
	'RS1801394': 'AG',
	'RS1256335': 'AA',
	'RS4654748': 'TT',
	'RS855791': 'AG',
	'RS4820268': 'AG',
	'RS11950646': 'AG',
	'RS33972313': 'CT',
	'RS6053005': 'CT',
	'RS6133175': 'AG',
	'RS1155563': 'CT',
	'RS2282679': 'GT',
	'RS7041': 'AC',
	'RS16846876': 'AT',
	'RS17467825': 'AG',
	'RS2242480': 'TC',
	'RS2209314': 'CT',
	'RS11126936': 'GT',
	'RS233804': 'AC',
	'RS4872479': 'GT',
	'RS117153535': 'CA',
	'RS675': 'AT',
	'RS1544410': 'CT',
	'RS492602': 'AG',
	'RS9606756': 'AG'
}

# 不同项目需要维护的数据 - 可与 Excel 数据一同维护，此处写死在代码中了
knowledge_base = {
	'Folic Acid': {
		'snps': {
			'RS1801133': {'GG': 64, 'AG': 128, 'AA': 256},
			'RS1801131': {'TT': 8, 'GT': 16, 'GG': 32},
			'RS1801394': {'AA': 1, 'AG': 2, 'GG': 4}
		},
		'ranges': [(0, 73.5, '正常，按需摄入叶酸'), (74, 77, '稍高，可补充叶酸'), (81, 82.5, '稍高，适量补充叶酸'), (97, 97.5, '稍高，适量补充叶酸'), (84, 84.5, '高，适量补充叶酸'), (98, 101, '高，适量补充叶酸'), (137, 165, '高，补充活性叶酸'), (265, 293, '极高，补充活性叶酸')]
	},
	'Vitamin B6': {
		'snps': {
			'RS1256335': {'AA': 0, 'AG': 1, 'GG': 2},
			'RS4654748': {'TT': 0, 'CT': 1, 'CC': 2}
		},
		'ranges': [(0, 1, '正常'), (1, 3, '稍高'), (3, 99, '高')]
	},
	'Iron': {
		'snps': {
			'RS855791': {'GG': 0, 'AG': 1, 'AA': 2},
			'RS4820268': {'GG': 0, 'AG': 1, 'AA': 2}
		},
		'ranges': [(0, 1, '正常'), (1, 3, '稍高'), (3, 99, '高')]
	},
	'Vitamin B2': {
		'snps': {
			'RS1801133': {'GG': 0, 'AG': 1, 'AA': 2}
		},
		'ranges': [(0, 1, '正常'), (1, 2, '稍高'), (2, 99, '高')]
	},
	'Vitamin C': {
		'snps': {
			'RS11950646': {'AA': 0, 'AG': 1, 'GG': 2},
			'RS33972313': {'CC': 0, 'CT': 2, 'TT': 2},
			'RS6053005': {'TT': 0, 'CT': 2, 'CC': 2},
			'RS6133175': {'GG': 0, 'AG': 2, 'AA': 2}
		},
		'ranges': [(0, 2, '正常'), (2, 6, '稍高'), (6, 99, '高')]
	},
	'Vitamin D': {
		'snps': {
			'RS1155563': {'TT': 0, 'CT': 1, 'CC': 2},
			'RS2282679': {'TT': 0, 'GT': 1, 'GG': 2},
			'RS7041': {'CC': 0, 'AC': 1, 'AA': 2},
			'RS16846876': {'AA': 0, 'AT': 1, 'TT': 2},
			'RS17467825': {'AA': 0, 'AG': 1, 'GG': 2},
			'RS2242480': {'TT': 0, 'CT': 0, 'CC': 2},
			'RS2209314': {'TT': 0, 'CT': 1, 'CC': 1}
		},
		'ranges': [(0, 4, '正常'), (4, 10, '稍高'), (13, 99, '高')]
	},
	'Zinc': {
		'snps': {
			'RS11126936': {'TT': 0, 'GT': 1, 'GG': 2},
			'RS233804': {'AA': 0, 'AC': 0, 'CC': 2},
			'RS4872479': {'TT': 0, 'GT': 1, 'GG': 2},
			'RS117153535': {'CC': 0, 'AC': 1, 'AA': 1}
		},
		'ranges': [(0, 2, '正常'), (2, 6, '稍高'), (6, 99, '高')]
	},
	'Vitamin E': {
		'snps': {
			'RS675': {'TT': 0, 'AT': 2, 'AA': 2}
		},
		'ranges': [(0, 2, '正常'), (2, 99, '高')]
	},
	'Calcium': {
		'snps': {
			'RS1544410': {'CC': 0, 'CT': 1, 'TT': 2}
		},
		'ranges': [(0, 1, '正常'), (1, 2, '稍高'), (2, 99, '高')]
	},
	'Vitamin B12': {
		'snps': {
			'RS1801133': {'GG': 0, 'AG': 1, 'AA': 2},
			'RS492602': {'GG': 0, 'AG': 2, 'AA': 2},
			'RS9606756': {'AA': 0, 'AG': 2, 'GG': 2},
		},
		'ranges': [(0, 2, '正常'), (2, 5, '稍高'), (5, 99, '高')]
	}
}

## 通用计算总分函数

def sum_calculate(snp_knowledge, user_input):
	sum = 0
	for k in snp_knowledge:
		## 用户位点返回时，如果是杂合，两个基因型顺序可能颠倒，但是是等价的，因此需要将基因型字符串排序，需要匹配知识库里位点说明的时候也需要注意
		sum = sum + snp_knowledge[k][''.join(sorted(user_input[k]))]
	return sum

## 项目结论算法
def calculate_case(sum, ranges):
	for this_range in ranges:
		if sum >= this_range[0] and sum < this_range[1]:
			return this_range[2]


## 结果变量
output = {}

## 开始计算，下方算法可以生成接口 2.1 需要的全部项目结果数据，但需要根据接口定义和需要的项目顺序重新组装结果 
for case in knowledge_base:
	snp_knowledge = knowledge_base[case]['snps']
	ranges = knowledge_base[case]['ranges']
	output[case] = calculate_case(sum_calculate(snp_knowledge, user_input), ranges)

print(output)

## 接口 2.2 只需计算单个项目（Case）的综合结论，再将位点与知识库中的位点说明进行匹配组装即可。

