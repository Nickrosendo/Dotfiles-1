from libqtile import bar, widget
from libqtile.layout import MonadTall, MonadWide, Max, Floating, bsp
from libqtile.config import Click, Drag, Group, Key, Screen, Match
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.extension import DmenuRun, WindowList, CommandSet

mod = "mod4"
terminal = "st"
terminal_alt = "alacritty"
browser = "tabbed -c vimb -e"
browser_alt = "firefox"
filemanager = "st -e vifm"
filemanager_alt = "pcmanfm"
email = "st -e neomutt"
musicplayer = "st -e cmus"
keys = [
    # launch and kill programs
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"),
    Key(
        [mod, "shift"],
        "t",
        lazy.spawn(terminal_alt),
        desc="Launch alternative terminal",
    ),
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
    Key(
        [mod, "shift"], "b", lazy.spawn(browser_alt), desc="Launch alternative browser"
    ),
    Key([mod], "m", lazy.spawn(musicplayer), desc="Launch kusicplayer"),
    Key([mod], "f", lazy.spawn(filemanager), desc="Launch filemanager"),
    Key(
        [mod, "shift"],
        "f",
        lazy.spawn(filemanager_alt),
        desc="Launch alternative filemanager",
    ),
    Key([mod], "e", lazy.spawn(email), desc="Launch neomutt"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    # qtile commands
    Key([mod], "c", lazy.restart(), desc="Restart qtile"),
    Key([mod, "shift"], "c", lazy.shutdown(), desc="Shutdown qtile"),
    # run prompts and menu
    Key([mod], "x", lazy.spawn("/home/sam/.config/xmenu/xmenu.sh")),
    Key([mod], "space", lazy.spawn("rofi -show drun")),
    Key([mod, "control"], "a", lazy.spawn("rofi -show window")),
    Key(
        [mod, "control"],
        "p",
        lazy.run_extension(
            CommandSet(
                commands={
                    "suspend": "systemctl suspend",
                    "shutdown": "systemctl poweroff",
                    "reboot": "systemctl reboot",
                },
            )
        ),
    ),
    # shift window focus
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    # move windows
    Key([mod, "control"], "j", lazy.layout.shuffle_down()),
    Key([mod, "control"], "k", lazy.layout.shuffle_up()),
    Key([mod, "control"], "h", lazy.layout.shuffle_left()),
    Key([mod, "control"], "l", lazy.layout.shuffle_right()),
    # resize windows
    Key([mod, "shift"], "h", lazy.layout.shrink()),
    Key([mod, "shift"], "l", lazy.layout.grow()),
    Key([mod, "shift"], "m", lazy.layout.maximize()),
    Key([mod, "shift"], "r", lazy.layout.normalize()),
    # layout modifires
    Key([mod], "n", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "control"], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "control"], "t", lazy.window.toggle_floating()),
    # brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc +5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec +5")),
    # Audio
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(" pulsemixer --change-volume +5")),
    Key([], "XF86AudioLowerVolume", lazy.spawn(" pulsemixer --change-volume -5")),
    # screenshots
    Key(
        [mod],
        "Print",
        lazy.spawn("escrotum '/home/sam/hdd/screenshots/%Y-%m-%d-%H%M%S_$wx$h_sc.png'"),
    ),
    Key(
        [mod, "control"],
        "Print",
        lazy.spawn(
            "escrotum -s '/home/sam/hdd/screenshots/%Y-%m-%d-%H%M%S_$wx$h_sc.png'"
        ),
    ),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # # mod1 + shift + letter of group = move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                # bar
                desc="move focused window to group {}".format(i.name),
            ),
        ]
    )

# borders
border_focus = "#5af78e"
border_width = 2
margin = 10
single_border_width = 0
single_margin = 10

# bar
layouts = [
    MonadTall(
        border_focus=border_focus,
        border_width=border_width,
        margin=margin,
        single_border_width=single_border_width,
        single_margin=single_margin,
        name="Tall",
    ),
    MonadWide(
        border_focus=border_focus,
        border_width=border_width,
        margin=margin,
        single_border_width=single_border_width,
        single_margin=single_margin,
        name="wide",
    ),
    bsp.Bsp(
        border_focus=border_focus,
        border_width=border_width,
        margin=margin,
        single_border_width=single_border_width,
        single_margin=single_margin,
        name="Grid",
    ),
    Max(
        border_focus=border_focus,
        border_width=border_width,
        margin=single_margin,
        single_border_width=0,
        single_margin=0,
        name="Full",
    ),
]

widget_defaults = dict(
    font="Hack Bold",
    fontsize=13,
    padding=3,
)
# calbacks
def run_htop(qtile):
    qtile.cmd_spawn("st -e htop")


def run_xmenu(qtile):
    qtile.cmd_spawn("/home/sam/.config/xmenu/xmenu.sh")


# bar color
bar_colors = [
    "#282a36",  # black
    "#ff5555",  # red
    "#5af78e",  # green
    "#f1fa8c",  # yellow
    "#57c7ff",  # blue
    "#ff6ac1",  # magenta
    "#8be9fd",  # cyan
    "#f1f1f0",  # white
    "#ffb86c",  # orange
    "#6272a4",  # purple
    "#44475a",  # light black
]
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(
                    filename="/home/sam/.config/qtile/icons/py.png",
                    margin=2,
                    mouse_callbacks={"Button1": run_xmenu},
                    background=bar_colors[0],
                ),
                widget.Sep(
                    linewidth=4,
                    foreground=bar_colors[0],
                    background=bar_colors[0],
                    size_percent=100,
                ),
                widget.CurrentLayout(
                    foreground=bar_colors[0], background=bar_colors[4]
                ),
                widget.Sep(
                    linewidth=10,
                    foreground=bar_colors[0],
                    background=bar_colors[0],
                    size_percent=100,
                ),
                widget.GroupBox(
                    margin_y=3,
                    margin_x=0,
                    padding_y=5,
                    padding_x=3,
                    borderwidth=3,
                    background=bar_colors[3],
                    active=bar_colors[1],
                    disable_drag=True,
                ),
                widget.Sep(
                    linewidth=10,
                    foreground=bar_colors[0],
                    background=bar_colors[0],
                    size_percent=100,
                ),
                widget.WindowName(foreground=bar_colors[5], background=bar_colors[0]),
                widget.Image(
                    filename="/home/sam/.config/qtile/icons/cpu.png",
                    background=bar_colors[5],
                    margin=2,
                    mouse_callbacks={"Button1": run_htop},
                ),
                widget.CPU(
                    format="CPU {freq_current}GHz {load_percent}%",
                    update_interval=5,
                    foreground=bar_colors[0],
                    background=bar_colors[5],
                    mouse_callbacks={"Button1": run_htop},
                ),
                widget.ThermalSensor(
                    background=bar_colors[5],
                    foreground=bar_colors[0],
                    update_interval=5,
                    mouse_callbacks={"Button1": run_htop},
                ),
                widget.Sep(
                    linewidth=4,
                    foreground=bar_colors[0],
                    background=bar_colors[0],
                    size_percent=100,
                ),
                widget.Image(
                    filename="/home/sam/.config/qtile/icons/memory.png",
                    background=bar_colors[3],
                    margin=1,
                    mouse_callbacks={"Button1": run_htop},
                ),
                widget.Memory(
                    format="Mem {MemUsed}MB ",
                    foreground=bar_colors[0],
                    background=bar_colors[3],
                    update_interval=5,
                    mouse_callbacks={"Button1": run_htop},
                ),
                widget.Sep(
                    linewidth=4,
                    foreground=bar_colors[0],
                    background=bar_colors[0],
                    size_percent=100,
                ),
                widget.Image(
                    filename="/home/sam/.config/qtile/icons/wifi.png",
                    background=bar_colors[4],
                    margin=3,
                ),
                widget.Wlan(
                    interface="wlp0s20f3",
                    format="{essid}",
                    disconnected_message="",
                    foreground=bar_colors[0],
                    background=bar_colors[4],
                ),
                widget.Net(
                    format="{interface}",
                    interface="enp0s20f0u1",
                    foreground=bar_colors[0],
                    background=bar_colors[4],
                ),
                widget.Sep(
                    linewidth=4,
                    foreground=bar_colors[0],
                    background=bar_colors[0],
                    size_percent=100,
                ),
                widget.Image(
                    filename="/home/sam/.config/qtile/icons/battery.png",
                    background=bar_colors[2],
                    margin=1,
                ),
                widget.Battery(
                    charge_char="AC",
                    discharge_char="",
                    low_foreground=bar_colors[1],
                    low_percentage=0.2,
                    format="{char} {percent:2.0%} ({hour:d}:{min:02d})",
                    update_interval=30,
                    background=bar_colors[2],
                    foreground=bar_colors[0],
                ),
                widget.Sep(
                    linewidth=4,
                    foreground=bar_colors[0],
                    background=bar_colors[0],
                    size_percent=100,
                ),
                widget.Image(
                    filename="/home/sam/.config/qtile/icons/brightness.png",
                    background=bar_colors[3],
                    margin=2,
                ),
                widget.Backlight(
                    backlight_name="intel_backlight",
                    format="{percent:2.0%}",
                    foreground=bar_colors[0],
                    background=bar_colors[3],
                    step=1,
                ),
                widget.Sep(
                    linewidth=4,
                    foreground=bar_colors[0],
                    background=bar_colors[0],
                    size_percent=100,
                ),
                widget.Image(
                    filename="/home/sam/.config/qtile/icons/vol.png",
                    background=bar_colors[3],
                    margin=4,
                ),
                widget.Volume(foreground=bar_colors[0], background=bar_colors[3]),
                widget.Sep(
                    linewidth=4,
                    foreground=bar_colors[0],
                    background=bar_colors[0],
                    size_percent=100,
                ),
                widget.Image(
                    filename="/home/sam/.config/qtile/icons/calendar.png",
                    background=bar_colors[6],
                    margin=4,
                ),
                widget.Clock(
                    format="%a %b %I:%M %p",
                    foreground=bar_colors[0],
                    background=bar_colors[6],
                ),
                widget.Systray(background=bar_colors[0]),
            ],
            size=20,
            opacity=1.0,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = Floating(
    float_rules=[
        {"wmclass": "confirm"},
        {"wmclass": "dialog"},
        {"wmclass": "download"},
        {"wmclass": "error"},
        {"wmclass": "file_progress"},
        {"wmclass": "notification"},
        {"wmclass": "splash"},
        {"wmclass": "toolbar"},
        {"wmclass": "confirmreset"},  # gitk
        {"wmclass": "makebranch"},  # gitk
        {"wmclass": "maketag"},  # gitk
        {"wname": "branchdialog"},  # gitk
        {"wname": "pinentry"},  # GPG key password entry
        {"wmclass": "ssh-askpass"},  # ssh-askpass
        {"wmclass": "Steam"},
        {"wmclass": "feh"},
        {"wmclass": "vlc"},
        {"wname": "Picture in picture"},
        {"wname": "FreeTube"},
        {"wname": "lutris"},
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"

# auto shifting programs to specified groups
groups = [
    Group("1"),
    Group("2"),
    Group("3"),
    Group("4", matches=[Match(wm_class=["Steam"])]),
    Group("5", matches=[Match(wm_class=["csgo_linux64"])]),
    Group("6"),
    Group("7"),
    Group("8"),
    Group("9"),
]

wmname = "Qtile"
