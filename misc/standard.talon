#(jay son | jason ): "json"
#(http | htp): "http"
#tls: "tls"
#M D five: "md5"
#word (regex | rejex): "regex"
#word queue: "queue"
#word eye: "eye"
#word iter: "iter"
#word no: "NULL"
#word cmd: "cmd"
#word dup: "dup"
#word shell: "shell".
zoom in: edit.zoom_in()
zoom out: edit.zoom_out()
zoom reset: edit.zoom_reset()
scroll up: edit.page_up()
scroll down: edit.page_down()
now copy: edit.copy()
now cut: edit.cut()
now paste: edit.paste()
now undo: edit.undo()
now redo: edit.redo()
now same paste: edit.paste_match_style()
now file: edit.save()
wipe: key(backspace)
(pad | padding):
	insert("  ")
	key(left)
slap: edit.line_insert_down()
