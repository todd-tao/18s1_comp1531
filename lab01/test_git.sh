#!/bin/bash
branches=`git branch | wc -l`
success=0
if [ "$branches" -eq 1 ]
then
	echo 'You did not create a branch'
	success=1
fi

commits=`git log --format='%p' | wc -w`
lines=`git log --format='%p' | wc -l`
if [ "$commits" -lt "$lines" ]
then
	echo 'You did not do a merge? :( (at least not on this branch)'
	success=1
fi

if [ "$success" -eq 0 ]
then
	echo "Git tests passed"
fi
echo
echo
exit $success
