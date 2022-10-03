from Levenshtein_Min_Distance_exe2_4 import min_edit_dist_ex2_4
from Levenshtein_Min_Distance import min_edit_dist
from Regex_Exercices import *
from Eliza import Eliza


def call_levenshtein():

	source = "intention"
	target = "execution"
	result = min_edit_dist(source, target)

	for r in range(len(result)):
		print(result[r])
pass

def call_regex_exercices_only_alphacharacters():
	source = "ertyuio"
	ret = exe__2_1__all_alpha_char(source)

	print(ret)
pass

def call_regex_exercices_lower_char_end__in_b():

	source = "ertyuiob"
	ret = exe__2_1__all_lower_char_end__in_b(source)

	print(ret)
pass

def call_regex_exercices_exe__2_1__bab():

	source = "babab"
	ret = exe__2_1__bab(source)

	print(ret)
pass

def call_regex_exercices_exe__2_2_repeated_words():

	source = "adilson adilson"
	print(source)

	ret = exe__2_2_repeated_words(source)
	print(ret)
pass

def call_regex_exe__2_2_startwithnumber_finishWithWord():

	source = "17637467564 sdjsihdsf bla"
	print(source)

	ret = exe__2_2_startwithnumber_finishWithWord(source)
	print(ret)
pass

def call_regex_exe__2_2_containsgrottoandraven_words():

	source = "grotto oajsa#$%ˆˆ*3456789 raven"
	print(source)

	ret = exe__2_2_containsgrottoandraven_words(source)
	print(ret)
pass

def call_regex_exe__2_2_firstword_in_a_register():

	source = "dirso bla tre"
	print(source)

	ret = exe__2_2_firstword_in_a_register(source)
	print(ret)
pass

def call_Eliza_Help_Desk():
	Eliza("Minha senha não funciona").parse_sentence()
pass


# [
# [0, 1, 2, 3, 4],
# [1, 1, 2, 3, 3],
# [2, 2, 1, 2, 3],
# [3, 2, 2, 2, 3],
# [4, 3, 3, 2, 3]
# ]
def call_min_distance_changed_ex2_4():

	source = "leda"
	target = "deal"

	mat = min_edit_dist_ex2_4(source, target)
	print(mat)
pass

def call_min_distance_changed_ex2_5():

	#	distance == 3
	source = "driver"
	target = "brief"

	mat = min_edit_dist_ex2_4(source, target)
	print(mat)
	print('--'*89)
	#	distance == 1
	target = "drivers"
	mat = min_edit_dist_ex2_4(source, target)
	print(mat)
pass


if __name__ == '__main__':
	call_min_distance_changed_ex2_5()
pass

