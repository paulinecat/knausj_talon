from talon import Context, actions
ctx = Context()
ctx.matches = r"""
os: windows
app: Figma
"""

@ctx.action_class('user')
class UserActions:
    def figma_toggle_ui(): actions.key('ctrl-\\')
    def figma_quick_actions(): actions.key('ctrl-/')

    def figma_move(): actions.key('v')
    def figma_frame(): actions.key('f')
    def figma_pen(): actions.key('p')
    def figma_pencil(): actions.key('shift-p')
    def figma_text(): actions.key('t')
    def figma_rectangle(): actions.key('r')
    def figma_ellipse(): actions.key('o')
    def figma_line(): actions.key('l')
    def figma_arrow(): actions.key('shift-l')
    def figma_comment(): actions.key('c')
    def figma_pick_color(): actions.key('i')
    def figma_slice(): actions.key('s')
    def figma_rulers(): actions.key('shift-r')
    def figma_layout_grids(): actions.key('ctrl-shift-4')
    def figma_layers_panel(): actions.key('alt-1')
    def figma_assets_panel(): actions.key('alt-2')
    def figma_design_panel(): actions.key('alt-8')
    def figma_prototype_panel(): actions.key('alt-9')
    def figma_inspect_panel(): actions.key('alt-0')

    def figma_zoom_in(): actions.key('ctrl-=')
    def figma_zoom_out(): actions.key('ctrl--')
    def figma_zoom_hundred(): actions.key('ctrl-0')
    def figma_zoom_fit(): actions.key('shift-1')
    def figma_zoom_selection(): actions.key('shift-2')
    def figma_zoom_previous_frame(): actions.key('shift-n')
    def figma_zoom_next_frame(): actions.key('n')
    def figma_previous_page(): actions.key('pageup')
    def figma_next_page(): actions.key('pagedown')
    def figma_find_previous_frame(): actions.key('home')
    def figma_find_next_frame(): actions.key('end')