#!/bin/sh

cat <<EOF | xmenu | sh &
All applications
	    Browsers
		    Brave		brave
		    Firefox		firefox
		    Vimb		vimb
	    Utilities
		    pcmanfm		pcmanfm
		    Nitrogen		nitrogen
		    Volume		pavucontrol
		    Apprearance		lxappearance
	    Games
		    Steam		prime-run steam
	    Graphics
		    VLC		vlc
		    Gimp		gimp
Configs
	Qtile		st -e nvim ~/.config/qtile/config.py
	Xmonad		st -e nvim ~/.xmonad/xmonad.hs
	Xmobar		st -e nvim ~/.config/xmobar/xmobar.config
	Xmenu		st -e nvim ~/.config/xmenu/xmenu.sh
	ST		st -e nvim ~/builds/st/config.def.h
	Nvim		st -e nvim ~/.config/nvim/init.vim
	Xinitrc		st -e nvim ~/.config/X11/.xinitrc
Network
	on		st -e nmcli radio wifi on
	off	st -e nmcli radio wifi off
	Nmtui		st -e nmtui
Screenshot
	Full		maim ~/hdd/screenshots/$(date +%s).png
	Select		maim -s ~/hdd/screenshots/$(date +%s).png
	copy		maim -s | xclip -selection clipboard -t image/png
Terminal (st)		st

Shutdown		poweroff
Reboot			reboot
Suspend			systemctl suspend
EOF