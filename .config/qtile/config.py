from typing import List
from libqtile import bar, widget
from libqtile.layout import MonadTall, Matrix, MonadWide, Max, Floating
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.extension import DmenuRun, WindowList

mod = "mod4"
terminal = "st"
browser = "brave"
keys = [
    Key([mod], "n", lazy.layout.next()),
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "n", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "c", lazy.restart(), desc="Restart qtile"),
    Key([mod], "x", lazy.spawn("/home/sam/.config/qtile/xmenu.sh")),
    Key([mod, "shift"], "c", lazy.shutdown(), desc="Shutdown qtile"),
    # system power
    Key([mod, "control"], "1", lazy.spawn(" systemctl suspend")),
    Key([mod, "control"], "2", lazy.spawn("systemctl poweroff")),
    Key([mod, "control"], "3", lazy.spawn("systemctl reboot")),
    # extension keymaps
    Key(
        [mod],
        "space",
        lazy.run_extension(
            DmenuRun(
                dmenu_prompt=">",
                dmenu_font="MesloLgs NF",
                background="#282a36",
                foreground="#f8f8f2",
                selected_background="#bd93f9",
                selected_foreground="#f8f8f2",
            )
        ),
    ),
    Key(
        [mod],
        "a",
        lazy.run_extension(
            WindowList(
                all_groups=True,
                background="#282a36",
                foreground="#f8f8f2",
                selected_background="#bd93f9",
                selected_foreground="#f8f8f2",
            )
        ),
    ),
    # move between windows
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    # shufle windows
    Key([mod, "control"], "j", lazy.layout.shuffle_down()),
    Key([mod, "control"], "k", lazy.layout.shuffle_up()),
    Key([mod, "control"], "h", lazy.layout.shuffle_left()),
    Key([mod, "control"], "l", lazy.layout.shuffle_right()),
    # resize windows
    Key([mod, "shift"], "j", lazy.layout.grow_down()),
    Key([mod, "shift"], "k", lazy.layout.grow_up()),
    Key([mod, "shift"], "h", lazy.layout.shrink()),
    Key([mod, "shift"], "l", lazy.layout.grow()),
    Key([mod, "shift"], "r", lazy.layout.normalize()),
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen()),
    # brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc +5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec +5")),
    # Audio
    Key([], "XF86AudioMute", lazy.spawn("ponymix toggle")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("ponymix increase 5")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("ponymix decrease 5")),
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
border_focus_p = "#bd93f9"
border_width_p = 2
margin_p = 6
single_border_width_p = 0
single_margin_p = 6

# bar
layouts = [
    MonadTall(
        border_focus=border_focus_p,
        border_width=border_width_p,
        margin=margin_p,
        single_border_width=single_border_width_p,
        single_margin=single_margin_p,
    ),
    Matrix(
        border_focus=border_focus_p,
        border_width=border_width_p,
        margin=margin_p,
        single_border_width=single_border_width_p,
        single_margin=single_margin_p,
    ),
    MonadWide(
        border_focus=border_focus_p,
        border_width=border_width_p,
        margin=margin_p,
        single_border_width=single_border_width_p,
        single_margin=single_margin_p,
    ),
    Max(
        border_focus=border_focus_p,
        border_width=border_width_p,
        margin=single_margin_p,
        single_border_width=single_border_width_p,
        single_margin=single_margin_p,
    ),
]

widget_defaults = dict(
    font="Hack Bold",
    fontsize=12,
    padding=3,
)
#calbacks
def run_htop(qtile):
    qtile.cmd_spawn("st -e htop")

def run_xmenu(qtile):
    qtile.cmd_spawn("/home/sam/.config/qtile/xmenu.sh")
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
]
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(filename="/home/sam/.config/qtile/py.png",
                    mouse_callbacks={"Button1":run_xmenu}),
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
                    font="San Francisco",
                    foreground=bar_colors[0],
                    background=bar_colors[4],
                    highlight_method="line",
                    highlight_color=bar_colors[7],
                    active=bar_colors[0],
                    this_current_screen_border=bar_colors[1],
                    this_screen_border=bar_colors[3],
                    other_current_screen_border=bar_colors[5],
                    other_screen_border=bar_colors[2],
                    padding=1,
                    rounded=False,
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
                    background=bar_colors[1],
                    margin=2,
                    mouse_callbacks = {"Button1":run_htop}
                ),
                widget.CPU(
                    format="CPU {freq_current}GHz {load_percent}%",
                    update_interval=5,
                    foreground=bar_colors[0],
                    background=bar_colors[1],
                    mouse_callbacks = {"Button1":run_htop}
                ),
                widget.ThermalSensor(
                    background=bar_colors[1],
                    foreground=bar_colors[0],
                    update_interval=5,
                    mouse_callbacks = {"Button1":run_htop}
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
                    mouse_callbacks = {"Button1":run_htop}
                ),
                widget.Memory(
                    format="Mem {MemUsed}MB ",
                    foreground=bar_colors[0],
                    background=bar_colors[3],
                    update_interval=5,
                    mouse_callbacks = {"Button1":run_htop}
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
                    charge_char="",
                    discharge_char="",
                    low_foreground="#ff5555",
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
            20,
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
        {"wmclass": "Steam"},  # ssh-askpass
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"
