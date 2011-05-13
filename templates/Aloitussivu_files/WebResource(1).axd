/* new styles */
.RadRotator_Default .rrClipRegion
{
	border: solid 1px #a7bac5;
}

/*================== The list ========================*/

.RadRotator_Default .rrClipRegion  .rrItemsList 
{
	float: left;
	padding: 0;
	margin: 0;
	list-style: none;          
}

/* For vertical carousel, not set, width defaults to auto */
/* Note if you explicitly set width to auto, this might cause */
/* problems with Safari */

.RadRotator_Default .rrButton
{
	background-image: url('WebResource.axd?d=muE4_iL3XRJic-O2fRDCTo0CQZB9aPse4SwLtLjThlbfRt_Ne1yufbwJqLJT8zoWx_Ce9cFH6pXNFcHxVkxkijPsTxxMdlo397iV6_PwrVCIwIBgi6yvmF6MSliWr7weooqwppGWDex85ELNvuRl0qogtcs1&t=634145324660000000');
	background-repeat: no-repeat;
	/*Button size is defined here, we use margins to position them too */
	height: 20px;
	width: 20px;
	line-height: 20px;
	/* Very important for the layout!*/	
}

.RadRotator_Default .rrButton.rrButtonUp
{
	background-position: 0 0;
	top: -20px;
	left: 50%;
	margin-left: -10px;
}

.RadRotator_Default .rrButton.rrButtonUp:hover
{
	background-position: -20px 0;
}

.RadRotator_Default .rrButton.rrButtonRight
{
	background-position: 0 -20px;
	margin-top: -10px;
	right: -20px;
	top: 50%;   
}

.RadRotator_Default .rrButton.rrButtonRight:hover
{
	background-position: -20px -20px;
}

.RadRotator_Default .rrButton.rrButtonDown
{
	background-position: 0 -40px;
	top:100%;
	left: 50%;
	margin-left: -10px;
}

.RadRotator_Default .rrButton.rrButtonDown:hover
{
	background-position: -20px -40px;
}

.RadRotator_Default .rrButton.rrButtonLeft
{
	background-position: 0 -60px;
	margin-top: -7px;
	left: -15px;
	top: 50%;
}

.RadRotator_Default .rrButton.rrButtonLeft:hover
{
	background-position: -20px -60px;
}

.RadRotator_Default .rrButton.rrButtonDisabled
{
	filter: alpha(opacity=20);
	opacity: .2;
	-moz-opacity: .2;
}

/* When LoadOnDemand */
.rrLoadingSign
{
    background: url('WebResource.axd?d=mP2RueW2ktKHCy7cc2L8_k2bXMEjSvu0danRJieF13StpzH-WNGKciNZSfRI02TQM9qQXcHHz765XaN0KeZS0wAOj0OJ9vWIp0tVQZc5lq2nWBtWiYJz4x5WVaylPYWykcEEl_eQCOb6jS_DymId4XTree81&t=634145324660000000') no-repeat center;
}
