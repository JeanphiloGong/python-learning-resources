#coding=utf-8
favorite_languages = {
    'jen': ['python','ruby'],
    'sarah':['c'],
    'adward':['ruby','go'],
    'phil':['python','haskell'],
    }
    
for name, languages in favorite_languages.items():
	
	
	for language in languages:
		if len(language) == 1:
			print("\n" + name.title() + "'s favorite language is:")
		else:
			print("\n" + name.title() + "'s favorite languages are:")
		print("\t" + language.title())
#always exist some problems in here
