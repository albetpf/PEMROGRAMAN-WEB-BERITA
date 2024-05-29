/**
 * @license Copyright (c) 2003-2021, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	config.extraPlugins = 'wordcount,notification';
	
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
};

config.wordcount = {

    // Whether or not you Show Remaining Count (if Maximum Word/Char/Paragraphs Count is set)
    showRemaining: false,
	
	// Whether or not you want to show the Paragraphs Count
    showParagraphs: true,

    // Whether or not you want to show the Word Count
    showWordCount: true,

    // Whether or not you want to show the Char Count
    showCharCount: false,
	
	// Whether or not you want to Count Bytes as Characters (needed for Multibyte languages such as Korean and Chinese)
	countBytesAsChars: false,

    // Whether or not you want to count Spaces as Chars
    countSpacesAsChars: false,

    // Whether or not to include Html chars in the Char Count
    countHTML: false,
    
    // Whether or not to include Line Breaks in the Char Count
    countLineBreaks: false,
	
	// Whether or not to prevent entering new Content when limit is reached.
	hardLimit: true,
	
	// Whether or not to to Warn only When limit is reached. Otherwise content above the limit will be deleted on paste or entering
    warnOnLimitOnly: false,

    // Maximum allowed Word Count, -1 is default for unlimited
    maxWordCount: -1,

    // Maximum allowed Char Count, -1 is default for unlimited
    maxCharCount: -1,
    
    // Maximum allowed Paragraphs Count, -1 is default for unlimited
    maxParagraphs: -1,

    // How long to show the 'paste' warning, 0 is default for not auto-closing the notification
    pasteWarningDuration: 0,
    

    // Add filter to add or remove element before counting (see CKEDITOR.htmlParser.filter), Default value : null (no filter)
    filter: new CKEDITOR.htmlParser.filter({
        elements: {
            div: function( element ) {
                if(element.attributes.class == 'mediaembed') {
                    return false;
                }
            }
        }
    })
};