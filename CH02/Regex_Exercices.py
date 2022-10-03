import re


def exe__2_1__all_alpha_char(source):

	pattern = re.compile("[a-zA-Z]+")
	contains_only_strings = pattern.fullmatch(source)

	return(contains_only_strings)
pass

def exe__2_1__all_lower_char_end__in_b(source):

	pattern = re.compile("[a-z]*b$")
	contains_only_strings = pattern.fullmatch(source)

	return(contains_only_strings)
pass


# Positive lookbehind
# (?<=<lookbehind_regex>)

# Positive lookahead
# (?=<lookahead_regex>)
# every a folowed and preceded by a b
def exe__2_1__bab(source):

	# (b + (ab +) +)?
	pattern = re.compile("(b+(ab+)+)")
	contains_only_strings = pattern.fullmatch(source)

	return(contains_only_strings)
pass



def exe__2_2_repeated_words(source):

	p = re.compile(r"\b(\w+)\s+\1\b")
	result = p.search(source)

	is_pattern_acceptable = False
	if result is not None:
		is_pattern_acceptable = True

	return(is_pattern_acceptable)
pass

def exe__2_2_startwithnumber_finishWithWord(source):

	# ^[0-9]*  .*  [a-zA-Z]+$
	p = re.compile(r"^[0-9]*.*[a-zA-Z]+$")
	result = p.search(source)

	is_pattern_acceptable = False
	if result is not None:
		is_pattern_acceptable = True

	return(is_pattern_acceptable)
pass

def exe__2_2_containsgrottoandraven_words(source):

	# ^[0-9]*  .*  [a-zA-Z]+$
	p = re.compile(r"\bgrotto+\b.*\braven+\b")
	result = p.search(source)

	is_pattern_acceptable = False
	if result is not None:
		is_pattern_acceptable = True

	return(is_pattern_acceptable)
pass


def exe__2_2_firstword_in_a_register(source):

	p = re.compile(r"\b([a-zA-Z]+)\b")
	result = p.search(source)
	register = result.groups()[0]

	is_pattern_acceptable = False
	if result is not None:
		is_pattern_acceptable = True

	return(is_pattern_acceptable)
pass