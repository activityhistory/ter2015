/**
 * ScreenshotsPrivacyFilterPreviewerController
 *
 * @description :: Server-side logic for managing Screenshotsprivacyfilterpreviewers
 * @help        :: See http://links.sailsjs.org/docs/controllers
 */

module.exports = {



  /**
   * `ScreenshotsPrivacyFilterPreviewerController.show()`
   * Show the page with the screenshots slider, and the smartslider wich higlight filtred screenshots
   */
  show: function (req, res) {
    res.view('Keywords', {title: "coucou", layout: null});
  }

};

