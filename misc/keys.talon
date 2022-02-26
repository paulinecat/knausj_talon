go <user.arrow_keys>: key(arrow_keys)
<user.letter>: key(letter)
(ship | uppercase) <user.letters> [(lowercase | sunk)]:
    user.insert_formatted(letters, "ALL_CAPS")
<user.symbol_key>: key(symbol_key)
<user.function_key>: key(function_key)
<user.special_key>: key(special_key)
<user.modifiers> <user.unmodified_key>: key("{modifiers}-{unmodified_key}")
press <user.modifiers>: key(modifiers)
key cam: "cmd"
key troll: "ctrl"
key (alt | all): "alt"
now quit: key(cmd-q)
now deep (paste | pace): key(cmd-shift-v)
now hide: key(cmd-m)
now close: key(cmd-w)
now new tab: key(cmd-t)
now new window: key(cmd-n)
now jump: key(cmd-k)
(aline | align | a line) right: key(cmd-])
(aline | align | a line) left: key(cmd-[)
screen up: key(cmd-y)
screen down: key(ctrl-e)