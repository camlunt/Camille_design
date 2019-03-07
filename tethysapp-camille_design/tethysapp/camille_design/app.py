from tethys_sdk.base import TethysAppBase, url_map_maker


class CamilleDesign(TethysAppBase):
    """
    Tethys app class for Camilles Design.
    """

    name = 'Camilles Design'
    index = 'camille_design:home'
    icon = 'camille_design/images/icon.gif'
    package = 'camille_design'
    root_url = 'camille-design'
    color = '#ffe65e'
    description = 'Shows PDF version of the project proposal and wireframe mockups'
    tags = '&quot;Proposal&quot;,&quot;Wireframe&quot;'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='camille-design',
                controller='camille_design.controllers.home'
            ),
            UrlMap(
                name='proposal',
                url='proposal',
                controller='camille_design.controllers.proposal'
            ),
            UrlMap(
                name='wireframes',
                url='wireframes',
                controller='camille_design.controllers.wireframes'
            ),
        )

        return url_maps
