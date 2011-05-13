/* new styles */
.RadRotator
{
	visibility:hidden; 	
}

.rrRelativeWrapper
{
	position: relative;
	margin:0 !important;/*MUST BE 0 for proper rendering*/
}

.rrClipRegion
{
	width: 100%;
	height: 100%;
	/* We change the width and height from the code, and then this setting becomes active! */
	overflow: hidden;
	position: absolute;
}

/*================== The list ========================*/

.rrClipRegion  .rrItemsList 
{
	float: left;
	padding: 0;
	margin: 0;
	list-style: none !important;          
}

.rrClipRegion  .rrItemsList li 
{ 
	float: left;
}

/* For vertical carousel, not set, width defaults to auto */
/* Note if you explicitly set width to auto, this might cause */
/* problems with Safari */

.RadRotator ul.rrVerticalList 
{
	padding: 0;
	margin: 0;
	list-style: none !important;
}

.RadRotator .rrVerticalList li
{ 
	float: none;
	margin-bottom: 0px;
	/* Force the LI to respect the HEIGHT specified */
	overflow: hidden;
	display: block;
}

.rrButton
{
	font-size: 1px;
	text-indent: -9999px;
	display: block;
	position: absolute;
	/*Button size is defined here, we use margins to position them too */
	height: 15px;
	width: 15px;
	line-height: 15px;
	/* Very important for the layout!*/	
	display: none; 
	outline: none;
}

.rrButton:hover
{
	filter: alpha(opacity=100);
	opacity: 1;
	-moz-opacity: 1;
	-ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";
}

.rrButton.rrButtonUp
{
	background-position: 0 0;
	top: -15px;
	left: 50%;
	margin-left: -8px;
}

.rrButton.rrButtonRight
{
	background-position: 0 -15px;
	margin-top: -8px;
	right: -16px;
	top: 50%;   
}

/* Fix button right position in Safari and Chrome */
@media screen and (-webkit-min-device-pixel-ratio:0)
	{
		.rrButtonRight
		{
			margin-right: -16px;
		}
	}

.rrButton.rrButtonDown
{
	background-position: 0 -30px;
	top:100%;
	left: 50%;
	margin-left: -8px;
	margin-top: 1px;
}

.rrButton.rrButtonLeft
{
	background-position: 0 -45px;
	margin-top: -7px;
	left: -15px;
	top: 50%;
}

.rrButton.rrButtonDisabled
{
	filter: alpha(opacity=20);
	opacity: .2;
	-moz-opacity: .2;
	-ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=20)";
}

.rrNoBorder .rrClipRegion
{
	border-width: 0px !important;
}

/* Needed because IE cannot position vertical LI items properly. In addition to this css, the UL's width needs to be EXPLICITLY set from code if IE or Safari */
html* .rrVerticalList li
{
	float: left !important;
}	