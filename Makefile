comment?=update
push:
	git status
	git add .
	git commit -m $(comment)
	git push 