tell application "Finder"
	set current_path to container of (path to me) as alias
end tell

set contentFile to ((current_path) as text) & "notes_content.txt"
set content to text of (read file contentFile as text)

tell application "Notes"
	if it is running then
		set var to true
	else
		set var to false
	end if
	make note
	set body of note "New Note" to content
	if var is false then
		quit
	end if
end tell