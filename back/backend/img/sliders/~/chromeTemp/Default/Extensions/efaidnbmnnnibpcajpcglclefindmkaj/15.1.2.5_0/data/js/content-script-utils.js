/*************************************************************************
* ADOBE CONFIDENTIAL
* ___________________
*
*  Copyright 2015 Adobe Systems Incorporated
*  All Rights Reserved.
*
* NOTICE:  All information contained herein is, and remains
* the property of Adobe Systems Incorporated and its suppliers,
* if any.  The intellectual and technical concepts contained
* herein are proprietary to Adobe Systems Incorporated and its
* suppliers and are protected by all applicable intellectual property laws,
* including trade secret and or copyright laws.
* Dissemination of this information or reproduction of this material
* is strictly forbidden unless prior written permission is obtained
* from Adobe Systems Incorporated.
**************************************************************************/
function isGoogleQuery(e){if(!e)return!1;try{if(new URL(e).host.startsWith("www.google."))return!0}catch(e){return!1}return!1}function sendMsg(e){"use strict";chrome.runtime.sendMessage(e)}function checkForThirdPartyCookiesStatus(e){const t=$("<iframe/>").attr("id","adbe-cookies-checker").css({display:"none"}).attr("src",chrome.extension.getURL("data/js/extn-utils.html"));t.on("load",s=>{t.remove(),e&&e()}),$("html").append(t)}function sendMsg(e){"use strict";chrome.runtime.sendMessage(e)}