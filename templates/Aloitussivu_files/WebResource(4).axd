/* RadWindow for ASP.NET AJAX Base Stylesheet */

/* MVC overrides */
.RadWindow table,
.RadWindow table td
{
	border:0;
	padding:0;
}

.RadWindow .rwTopResize
{
	font-size: 1px;
	line-height: 4px;
	width: 100%;
	height: 4px;
	background-position: 0 -31px;
	background-repeat: repeat-x;
}

.RadWindow .rwStatusbarRow .rwCorner
{
    background-repeat: no-repeat;
}

.RadWindow .rwStatusbarRow .rwBodyLeft
{
    background-position: -16px 0;
}

.RadWindow .rwStatusbarRow .rwBodyRight
{
    background-position: -24px 0;
}

.RadWindow .rwStatusbar
{
	height: 22px;
	background-position: 0 -113px;
	background-repeat: repeat-x;
}

.RadWindow .rwStatusbar div
{
    width: 18px; 
	height: 18px;
	padding: 0 3px 0 0;
	background-position: 0 -94px;
	background-repeat: no-repeat;
}

.RadWindow .rwTable
{
    width: 100%;
    height: 100%;
    table-layout: auto; /* fixes the dimensions under IE */
}

.RadWindow table td
{
	padding: 0; 
	margin: 0;
	border-collapse: collapse;
	vertical-align: top;
}

.RadWindow .rwCorner
{
    width: 8px;
}

.RadWindow .rwTopLeft,
.RadWindow .rwTopRight,
.RadWindow .rwTitlebar,
.RadWindow .rwFooterLeft,
.RadWindow .rwFooterRight,
.RadWindow .rwFooterCenter
{
    height: 8px;
	font-size: 1px;
    background-repeat: no-repeat;
    line-height: 1px;
}

.RadWindow .rwBodyLeft,
.RadWindow .rwBodyRight
{
	background-repeat: repeat-y;
}

.RadWindow .rwBodyRight
{
    background-position: -8px 0;
}

.RadWindow .rwTopLeft
{
    background-position: 0 0;
}

.RadWindow .rwTopRight
{
    background-position: -8px 0;
}

.RadWindow table .rwTitlebar
{
	background-repeat: repeat-x;
	background-position: 0 -31px;
	-moz-user-select: none;
}

.RadWindow .rwFooterLeft
{
	background-position: 0 -62px;
}

.RadWindow .rwFooterRight
{
	background-position: -8px -62px;
}

.RadWindow .rwFooterCenter
{
	background-repeat: repeat-x;
	background-position: 0 -70px;
}

.RadWindow .rwTitlebarControls
{
	width: 100%;
    height: 27px;
}

.RadWindow .rwWindowContent
{
	height: 100% !important; /* very important property, especially for opera */
	background: white;
}

/* Support for displayng the rwLoading image in the iframe's parent TD */
.RadWindow td.rwLoading
{
    background-repeat: no-repeat;
    background-position: center;
}

/* Support for displaying rwLoading image in the status bar  */
.RadWindow .rwStatusbar .rwLoading
{	
	background-repeat: no-repeat;
}

.RadWindow .rwStatusbar .rwLoading
{
	padding-left: 30px;
}

.RadWindow td.rwStatusbar input
{
    font: normal 12px "Segoe UI", Arial, Verdana, Sans-serif;
    padding: 4px 0 0 3px;
    margin: 0;
    border: 0 !important;
    width: 100%;	
    height: 18px;
    line-height: 18px;
	background-color: transparent !important; 
	background-repeat: no-repeat !important;
	background-position: left center !important;
	cursor: default;
	-moz-user-select: none;
	overflow: hidden; 
	text-overflow: ellipsis;
	display: block; 
	float: left;
	vertical-align: middle;
}

.RadWindow .rwControlButtons
{
	padding: 0; 
	margin: 2px 0 0 0;
	list-style: none; 
	white-space: nowrap;	
	float: right; 
}

.RadWindow .rwControlButtons li
{
	float: left;
	padding: 0 1px 0 0;
}

.RadWindow .rwControlButtons a
{
	width: 30px; 
	height: 21px; 
	line-height: 1px; 
	font-size: 1px;
	cursor: default;
	background-repeat: no-repeat;
	display: block; 
	text-decoration: none;
	outline: none;
}

.RadWindow .rwControlButtons span
{
	display: block;	
}

/* reload button */
.RadWindow  .rwReloadButton
{
	background-position: -120px 0;
}

.RadWindow .rwReloadButton:hover
{
	background-position: -120px -21px;
}

/* unpin button */
.RadWindow .rwPinButton
{
	background-position: -180px 0;
}

.RadWindow .rwPinButton:hover
{
	background-position: -180px -21px;
}

/* pin button */
.RadWindow .rwPinButton.on
{
	background-position: -150px 0;
}

.RadWindow .rwPinButton.on:hover
{
	background-position: -150px -21px;
}

/* minimize button */
.RadWindow .rwMinimizeButton
{
	background-position: 0 0;
}

.RadWindow .rwMinimizeButton:hover
{
	background-position: 0 -21px;
}

/* maximize button */
.RadWindow .rwMaximizeButton
{
	background-position: -60px 0;
}

.RadWindow .rwMaximizeButton:hover
{
	background-position: -60px -21px;
}

/* close button */
.RadWindow .rwCloseButton
{
	background-position: -90px 0;
}

.RadWindow .rwCloseButton:hover
{
	background-position: -90px -21px;
}

/* restore button */
.RadWindow.rwMaximizedWindow .rwMaximizeButton,
.RadWindow.rwMinimizedWindow .rwMinimizeButton
{
	background-position: -30px 0;
}

.RadWindow.rwMaximizedWindow .rwMaximizeButton:hover,
.RadWindow.rwMinimizedWindow .rwMinimizeButton:hover
{	
	background-position: -30px -21px;
}

.RadWindow .rwIcon
{
    display: block;
	background-repeat: no-repeat;
	background-position: 0 -78px;
	width: 16px; 
	height: 16px;
	cursor: default;
	margin: 5px 5px 0 0;
}

.RadWindow .rwTitleRow em
{
	font: normal bold 12px "Segoe UI", Arial;
	color: black;
	padding: 5px 0 0 1px;	
	overflow: hidden; 
	text-overflow: ellipsis; 
	white-space: nowrap; 
	float: left;	
}

.RadWindow_rtl .rwControlButtons
{
	float: left; 
}

div.RadWindow_rtl .rwControlButtons li
{
	float: right;
}

.RadWindow.rwInactiveWindow .rwTitlebarControls
{
	position: static;
}

.RadWindow .rwDialogPopup
{
	margin: 16px;
	color: black;	
	padding: 0px 0px 16px 50px;
	font: normal 12px "Segoe UI", Arial, Verdana;
	cursor: default;
}

.rwDialogPopup .rwPopupButton
{
    margin: 0;
}

/*.rwDialogPopup .rwPopupButton:focus,
.rwDialogPopup .rwPopupButton:active
{
    border: dotted 1px #999;                        
}*/

.rwDialogPopup .rwPopupButton,
.rwDialogPopup .rwPopupButton span
{
	display: block; 
	float: left;
}

.RadWindow .rwControlButtons a
{
    text-indent: -3333px;
    overflow: hidden;
    text-align:center;
}

html:first-child .RadWindow ul
{
    float: right; 
    border: solid 1px transparent;
}

.RadWindow .rwDialogText
{
    text-align: left;
}

.RadWindow.rwMinimizedWindow .rwPinButton,
.RadWindow.rwMinimizedWindow .rwReloadButton,
.RadWindow.rwMinimizedWindow .rwMaximizeButton,
.RadWindow.rwMinimizedWindow .rwTopResize
{
    display: none !important;
}

.RadWindow .rwDialogInput
{
	font: normal 12px "Segoe UI", Arial, Verdana;
	color: black;
	width: 100%;
	display: block;
	margin: 8px 0;
}

.RadWindow .rwWindowContent .radconfirm,
.RadWindow .rwWindowContent .radalert
{
    background-color: transparent;
	background-position: left center;
	background-repeat: no-repeat;
}

.RadWindow .rwWindowContent .radconfirm
{
    background-image: url('WebResource.axd?d=epjDr7P4aMdSE1GEPppkSFBcFQPtxDD5OnOuIntQ7MhhwNFdnXHWTC9Wk2BtICF9dvf3WZoWOEuYbOiXdStDNOigPBRT41B-faDrrXE-CHzcY4xErIiG74zSTHA2CyVfFqMMgssR-8lTwbeRMp6la485Eq01&t=634145324660000000');	
}

.RadWindow .rwWindowContent .radalert
{
    background-image: url('WebResource.axd?d=Wbfn2dqDGSg9-x4KoUvdUoAwyQzQsjeytzdtL5oYXbVJSa1u9ESC9dcyBT9JvyJwAQm4xZWXDhPQYaUOJzYbtWF8ngBuyHpV3bqoPOqshIVDAGrImX6GMN7Loibs-knua65YLPXO_iYRe32SwiKkscFhvLs1&t=634145324660000000');	
}

.RadWindow .rwWindowContent .radprompt
{
	padding: 0;
}

.RadWindow .rwPopupButton,
.RadWindow .rwPopupButton span
{
	text-decoration: none;
	color: black;
	line-height: 21px;
	height: 21px;
	cursor: default;
}

.RadWindow .rwPopupButton
{
	background-repeat: no-repeat;
	background-position: 0 -136px; 
	padding: 0 0 0 3px;
	margin: 8px 8px 8px 0;
}

.RadWindow .rwWindowContent .rwPopupButton .rwOuterSpan
{
    background-repeat: no-repeat;
	background-position: right -136px; 
	padding: 0 3px 0 0;
}

.RadWindow .rwWindowContent .rwPopupButton .rwInnerSpan
{
	background-repeat: repeat-x;
	background-position: 0 -157px; 
	padding: 0 12px;
}

.RadWindow .rwWindowContent .rwPopupButton:hover
{
	background-position: 0 -178px; 
	padding: 0 0 0 3px;
	margin: 8px 8px 8px 0;
}

.RadWindow .rwWindowContent .rwPopupButton:hover .rwOuterSpan
{
	background-position: right -178px; 
	padding: 0 3px 0 0;
}

.RadWindow .rwWindowContent .rwPopupButton:hover .rwInnerSpan
{
	background-position: 0 -199px; 
	padding: 0 12px;
}

.RadWindow .rwStatusbarRow .rwBodyLeft
{
    background-position: -16px 0;
}

.RadWindow .rwStatusbarRow .rwBodyRight
{
    background-position: -24px 0;
}

.RadWindow.rwMinimizedWindow .rwContentRow,
.RadWindow.rwMinimizedWindow .rwStatusbarRow
{
	display: none;
}

.RadWindow.rwMinimizedWindow table.rwTitlebarControls 
{
	margin-top: 4px;
}

.RadWindow.rwMinimizedWindow .rwControlButtons
{
    width: 66px !important;
}

.RadWindow.rwMinimizedWindow em
{
	width: 90px;
}

.RadWindow.rwMinimizedWindow,
.rwMinimizedWindowOverlay
{
    width: 200px !important;
    height: 30px !important;
    overflow: hidden !important;
    float: left !important;
}

.RadWindow.rwMinimizedWindow .rwCorner.rwTopLeft
{
	background-position: 0 -220px;
	background-repeat: no-repeat; 
}

.RadWindow.rwMinimizedWindow .rwCorner.rwTopRight
{
	background-position: -8px -220px;
	background-repeat: no-repeat; 
}

.RadWindow.rwMinimizedWindow .rwTitlebar
{
    background-position: 0 -250px !important; /* Should be !important because of IE6 */
    background-repeat: repeat-x;
}

.RadWindow.rwInactiveWindow .rwCorner,
.RadWindow.rwInactiveWindow .rwTitlebar,
.RadWindow.rwInactiveWindow .rwFooterCenter
{
	filter: progid:DXImageTransform.Microsoft.Alpha(opacity=65) !important;
	opacity: .65 !important; 
	-moz-opacity: .65 !important;
	-ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=65)";
}

/* stop the control buttons from stretching in IE8 */
.RadWindow ul.rwControlButtons span
{
    display /*\**/: none\9
}

/* css for window's top corners when visibletitlebar is set to false */
div.RadWindow.rwNoTitleBar tr.rwTitleRow td.rwTopLeft
{
    background-position: 0 -280px;
}

div.RadWindow.rwNoTitleBar tr.rwTitleRow td.rwTitlebar
{
    background-position: 0 -288px;
    background-repeat: repeat-x;
}

div.RadWindow.rwNoTitleBar tr.rwTitleRow td.rwTopRight
{
    background-position: -8px -280px;
}

div.RadWindow.rwNoTitleBar div.rwTopResize
{
    background: none;
}

/* Window Horizontal Shadows */

.RadWindow .rwShadow .rwTopLeft, 
.RadWindow .rwShadow .rwTopRight,
.RadWindow.rwMinimizedWindow .rwShadow .rwCorner.rwTopLeft,
.RadWindow.rwMinimizedWindow .rwShadow .rwCorner.rwTopRight
{
	width: 15px !important; 
}

.RadWindow .rwShadow .rwTopLeft, 
.RadWindow .rwShadow .rwTopRight 
{
height: 38px;	
}

.RadWindow .rwShadow .rwTopLeft,
.RadWindow.rwMinimizedWindow .rwShadow .rwCorner.rwTopLeft 
{
background-position: 0 -297px !important;
}

.RadWindow .rwShadow .rwTopRight,
.RadWindow.rwMinimizedWindow .rwShadow .rwCorner.rwTopRight
{
background-position: 0 -335px !important;
}

.RadWindow .rwShadow .rwTopResize 
{
	height: 8px;
	background-position: 0 -376px !important;
}

.RadWindow .rwShadow .rwTitlebar,
.RadWindow.rwMinimizedWindow .rwShadow .rwTitlebar 
{
	height: 30px !important; 
	background-position: 0 -391px !important; /* Should be !important because of IE6 */
	background-repeat: repeat-x !important;
}

.rwInactiveWindow.rwMinimizedWindow 
{
	height: 29px\9 !important;
}

* html .rwInactiveWindow.rwMinimizedWindow 
{
	height: 30px !important;
}

.RadWindow .rwShadow .rwFooterLeft, 
.RadWindow .rwShadow .rwFooterRight, 
.RadWindow .rwShadow .rwFooterCenter 
{
	height: 14px; 
}
.RadWindow .rwShadow .rwFooterLeft 
{
	width: 15px; 
	background-position: 0 -431px;
}
.RadWindow .rwShadow .rwFooterCenter 
{
	background-position: 0 -461px;
	background-repeat: repeat-x;
}
.RadWindow .rwShadow .rwFooterRight 
{
	width: 15px; 
	background-position: 0 -446px;
}

/* Window Vertical Shadows */

.RadWindow .rwShadow .rwBodyLeft,
.RadWindow .rwShadow .rwBodyRight
{
	width: 15px;
	background-repeat: repeat-y; 
}

.RadWindow .rwShadow .rwBodyLeft 
{
	background-position: -33px 0;
}

.RadWindow .rwShadow .rwBodyRight
{
	background-position: -52px 0;
}

.RadWindow .rwShadow em 
{
	padding: 9px 0 0 1px;
}


.RadWindow .rwShadow .rwIcon 
{
	margin: 8px 5px 0 1px;
}


/* Shadows minimzed specific style */

.RadWindow.rwMinimizedWindow .rwShadow .rwCorner.rwTopLeft,
.RadWindow.rwMinimizedWindow .rwShadow .rwCorner.rwTopRight
{
height: 1px !important;
}


.RadWindow.rwMinimizedWindowShadow
{
    overflow: visible !important;
}

.RadWindow.rwMinimizedWindowShadow .rwTable
{
    height: auto !important;
     width: 210px !important;
}

.RadWindow.rwMinimizedWindow .rwShadow .rwFooterLeft 
{
	background-position: 0 -432px;
}
.RadWindow.rwMinimizedWindow .rwShadow .rwFooterCenter 
{
	background-position: 0 -462px;
}
.RadWindow.rwMinimizedWindow .rwShadow .rwFooterRight 
{
	background-position: 0 -447px;
}

.RadWindow.rwMinimizedWindowShadow .rwShadow .rwTitlebarControls 
{
	display: block;
}

.RadWindow.rwMinimizedWindowShadow .rwShadow .rwTitlebarControls .rwControlButtons .rwPinButton,
.RadWindow.rwMinimizedWindowShadow .rwShadow .rwTitlebarControls .rwControlButtons .rwReloadButton,
.RadWindow.rwMinimizedWindowShadow .rwShadow .rwTitlebarControls .rwControlButtons .rwMaximizeButton,
.RadWindow.rwMinimizedWindowShadow .rwShadow .rwContentRow,
.RadWindow.rwMinimizedWindowShadow .rwShadow .rwStatusbarRow
{
	display: none !important;
}

.rwMinimizedWindowShadow .rwShadow .rwTopLeft, 
.rwMinimizedWindowShadow .rwShadow .rwTopRight,
.rwMinimizedWindowShadow .rwShadow .rwFooterLeft, 
.rwMinimizedWindowShadow .rwShadow .rwFooterRight, 
.rwMinimizedWindowShadow .rwShadow .rwFooterCenter,
.rwMinimizedWindowShadow .rwShadow .rwTopResize 
{
	cursor: default !important;
}

div.RadWindow_rtl table.rwShadow .rwControlButtons li
{
	float: right;
}

