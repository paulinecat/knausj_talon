from talon import Module

mod = Module()
apps = mod.apps
apps.figma = "app.name: Figma"

@mod.action_class
class figma_actions:
    def figma_toggle_ui():
        """Show/hide sidebars"""

    def figma_quick_actions():
        """Quick actions bar"""

    def figma_move():
        """Move tool"""

    def figma_frame():
        """Frame tool"""

    def figma_pen():
        """Pen tool"""

    def figma_pencil():
        """Pencil tool"""

    def figma_text():
        """Text tool"""

    def figma_rectangle():
        """Rectangle tool"""

    def figma_ellipse():
        """Ellipse tool"""

    def figma_line():
        """Line tool"""

    def figma_arrow():
        """Arrow tool"""

    def figma_comment():
        """Add comment"""

    def figma_pick_color():
        """Pick color"""

    def figma_slice():
        """Slice tool"""

    def figma_rulers():
        """Rulers"""

    def figma_layout_grids():
        """Layout grids"""

    def figma_layers_panel():
        """Open layers panel"""

    def figma_assets_panel():
        """Open assets panel"""

    def figma_design_panel():
        """Open design panel"""

    def figma_prototype_panel():
        """Open prototype panel"""

    def figma_inspect_panel():
        """Open inspect panel"""

    def figma_zoom_in():
        """Zoom in"""

    def figma_zoom_out():
        """Zoom out"""

    def figma_zoom_hundred():
        """Zoom to 100%"""

    def figma_zoom_fit():
        """Zoom to fit"""

    def figma_zoom_selection():
        """Zoom to selection"""

    def figma_zoom_previous_frame():
        """Zoom to previous frame"""

    def figma_zoom_next_frame():
        """Zoom to next frame"""

    def figma_previous_page():
        """Previous page"""

    def figma_next_page():
        """Next page"""

    def figma_find_previous_frame():
        """Find previous frame"""

    def figma_find_next_frame():
        """Fine next frame"""