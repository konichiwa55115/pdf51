# copyright ยฉ๏ธ 2021 nabilanavab
file_name = "lang/eng.py"


from configs.config   import settings

# REPLY MESSAGE FOR BROKEN WORKS
RESTART = {
    "msg" : """โ  `๐๐๐๐๐๐๐๐ ๐๐๐๐๐๐๐๐๐`โ :\n__pวสษนษสsวษน ษนวสษนวs__ \n
I noticed that your work was also in queue

Can you please try again..!""",
    "btn" : { "๐ถ CLOSE ๐ถ" : "close|mee" }
}

# PM WELCOME MESSAGE (HOME A, B, C, D...)
HOME = {
    "HomeA" : "ุงูุณูุงู ุนูููู ูุง   {}..!!\n"
"ูุฑุญุจุงู ุจู ูู  {}.!\n\n"

"ุณุฃููู ุจูุณุงุนุฏุชู ูู ูุต ู ุฏูุฌ ู ุชุญููู ูููุงุช ุงููpdf ุงูุฎุงุตุฉ ุจู ู ูููุฒุงุช ุฃุฎุฑู \n\n"






"ููุท ุฃุฑุณู ููู pdf ูุจุฏุฃ ุงูุนูู . ุฃู ุฃุฑุณู ูุฌููุนุฉ ุตูุฑ ูุฏูุฌูุง ูู ููู pdf \n\n"


"ูุจููุฉ ุงูุจูุชุงุช ููุง \n\n https://t.me/ibnAlQyyim/1120 \n\n ",
    "HomeACB" : {
        "โ๏ธ SETTINGS โ๏ธ" : "Home|B",
        "๐ LANGUAGE ๐" : "set|lang",
        "โ ๏ธ HELP โ ๏ธ" : "Home|C",
        "๐ข CHANNEL ๐ข" : f"{str(settings.OWNED_CHANNEL)}",
        "๐ SOURCE CODE ๐" : f"{str(settings.SOURCE_CODE)}",
        "โ ADD IN GROUP โ" : "https://t.me/{}?startgroup=True"
    },
    "HomeAdminCB" : {
        "โ๏ธ SETTINGS โ๏ธ" : "Home|B",
        "๐ LANGUAGE ๐" : "set|lang",
        "โ ๏ธ HELP โ ๏ธ" : "Home|C",
        "๐ข CHANNEL ๐ข" : f"{str(settings.OWNED_CHANNEL)}",
        "๐ SOURCE CODE ๐" : f"{str(settings.SOURCE_CODE)}",
        "๐ฝ STATUS ๐ฝ" : f"status|home",
        "โ ADD IN GROUP โ" : "https://t.me/{}?startgroup=True",
        "๐ถ CLOSE ๐ถ" : "close|mee"
    },
    "HomeB" : """SETTINGS PAGE โ๏ธ

USER NAME   : {}
USER ID           : {}
USERNAME    : {}
JOIN DATE      : {}

LANGUAGE    : {}
API                    : {}
THUMB            : {}
CAPTION         : {}
FILE NAME      : {}""",
    "HomeBCB" : {
        "๐ THUMB ๐" : "set|thumb",
        "๐ NAME ๐" : "set|fname",
        "๐ฉ API ๐ฉ" : "set|api",
        "๐ CAPTION ๐" : "set|capt",
        "ยซ BACK TO HOME ยซ" : "Home|B2A"
    },
    "HomeC" : """**Some of the main features are:**
 
 โ ```Create a PDF from your images: simply send it in bot pms [png, jpg, jpeg]```
 โ ```Extract the text from the PDF: Helps to extract the text from the PDF file and send as separate message.```
 โ ```Convert the PDF to another file format: [images, txt, html, json, tar, rar]```
 โ ```Merge multiple PDFs into one: Multiple PDF files to combine into a single file```
 โ ```Split a PDF into separate pages: Large PDF file to split it into separate ones```
 โ ```Extract images from the PDF: [all,range,pages] as image, doc, zip, rar```
 โ ```Helps to reduce size by optimizing the images. Useful in sending file via email when it's too large```
 โ ```Fetches Metadata: title of the document, the author, the subject, the keywords associated with the document, and the creation and modification dates```
 โ ```Encrypt/Decrypt Pdfs Using passwords, Websites to Pdf, Rotate, Rename, stamb..```
 โ ```WaterMark, Combine, Zoom, Draw, Add/Delete pages, Ocr pdf..```
 โ ```text messages to pdf files, and Much More.. ๐```""",
    "HomeCCB" : {
        "ยซ BACK HOME ยซ" : "Home|A",
        "๐ INSTRUCTIONS ๐" : "Home|D"
    },
    "HomeD" : """`As you know, this is a free service, I cannot guarantee how long I can maintain this service..`๐
 
โ ๏ธ INSTRUCTIONS โ ๏ธ:
 โ ```Please note that spamming is generally not tolerated and can result in the user or bot being banned from the service```
 โ ```Wait for the bot to process the file: The bot will process the PDF file and perform the requested action. This may take a few minutes, depending on the size of the file and the complexity of the action being performed.```
 โ ```Once the bot has completed the action, it will send you the results. If the action was successful, you will receive the output. If the action was not successful, the bot will let you know and provide any relevant error messages.```
 โ ```Any user found to be distributing or sharing pornographic content on the bot will be permanently banned```
**Send any image to start:** ๐""",
    "HomeDCB" : {
        "โ ๏ธ HELP โ ๏ธ" : "Home|C",
        "ยป BACK HOME ยป" : "Home|A"
    }  
}

# GROUP WELCOME MESSAGE
HomeG = {
    "HomeA" : HOME['HomeA'],
    "HomeACB" : {
        "๐ LANGUAGE ๐" : "set|lang",
        "๐ก๏ธ HELP ๐ก๏ธ": "Home|C",
        "๐ข CHANNEL ๐ข" : f"{str(settings.OWNED_CHANNEL)}",
        "๐ SOURCE CODE ๐": f"{settings.SOURCE_CODE}",
        "๐ถ CLOSE ๐ถ" : "close|mee",
    }
}

SETTINGS = {
    "lang" : "Now, Select any language..",
    "default" : ["DEFAULT โ", "CUSTOM โ"],
    "cant" : "This feature cannot be used โ",
    "wait" : { "Waiting.. ๐ฅฑ" : "nabilanavab" },
    "feedbtn" : { "Report any bugs you find!" : settings.REPORT },
    "chgLang" : {"SETTING โ๏ธ ยป CHANGE LANG ๐" : "nabilanavab"},
    "askApi" : "\n\nOpen the **Below** link and Send me the secret code:",
    "waitApi" : { "Open link โ" : "https://www.convertapi.com/a/signin" },
    "error" : "Something went wrong while retrieving data from the database",
    "result" : ["Settings cannot be updated โ", "Settings Updated Successfully โ"],
    "back" : [{ "ยซ BACK TO HOME ยซ" : "Home|B2S" }, { "ยซ BACK TO HOME ยซ" : "Home|B2A" }],
    "feedback" : "Bug warning! If my texts sound weird, it's probably Google Translate's fault."
                 "\n\nReport a BUG in {} Lang:\n`โข Specify Lang\nโข Error Message\nโข New Message`",
    "ask" : [
        "Now, Send me..",
        "Now, Send me.. ๐\n\nFast.! I have no more time to go over the text.. ๐\n\n/cancel: to cancel"
    ],
    "thumb" : [
        {
            "SETTING โ๏ธ ยป THUMBNAIL ๐ท" : "nabilanavab",
            "โป ADD โป" : "set|thumb+",
            "ยซ BACK TO HOME ยซ" : "Home|B"
        },
        {
            "SETTING โ๏ธ ยป THUMBNAIL ๐ท" : "nabilanavab",
            "โป CHANGE โป" : "set|thumb+",
            "๐ DELETE ๐" : "set|thumb-",
            "ยซ BACK TO HOME ยซ" : "Home|B2S"
        }
    ],
    "fname" : [
        {
            "SETTING โ๏ธ ยป FNAME ๐ท" : "nabilanavab",
            "โป ADD โป" : "set|fname+",
            "ยซ BACK TO HOME ยซ" : "Home|B2S"
        },
        {
            "SETTING โ๏ธ ยป FNAME ๐ท" : "nabilanavab",
            "โป CHANGE โป" : "set|fname+",
            "๐ DELETE ๐" : "set|fname-",
            "ยซ BACK TO HOME ยซ" : "Home|B2S"
        }
    ],
    "api" : [
        {
            "SETTING โ๏ธ ยป API ๐ท" : "nabilanavab",
            "โป ADD โป" : "set|api+",
            "ยซ BACK TO HOME ยซ" : "Home|B2S"
        },
        {
            "SETTING โ๏ธ ยป API ๐ท" : "nabilanavab",
            "โป CHANGE โป" : "set|api+",
            "๐ DELETE ๐" : "set|api-",
            "ยซ BACK TO HOME ยซ" : "Home|B2S"
        }
    ],
    "capt" : [
        {
            "SETTING โ๏ธ ยป CAPTION ๐ท" : "nabilanavab",
            "โป ADD โป" : "set|capt+",
            "ยซ BACK TO HOME ยซ" : "Home|B2S"
        },
        {
            "SETTING โ๏ธ ยป CAPTION ๐ท" : "nabilanavab",
            "โป CHANGE โป" : "set|capt+",
            "๐ DELETE ๐" : "set|capt-",
            "ยซ BACK TO HOME ยซ" : "Home|B2S"
        }
    ]
}

BOT_COMMAND = {
    "start" : "Welcome message..",
    "txt2pdf" : "Create text PDF's"
}

STATUS_MSG = {
    "_HOME" : {
        "๐ โ SERVER โ ๐" : "nabilanavab",
        "๐ถ STORAGE ๐ถ" : "status|server",
        "๐ฅฅ DATABASE ๐ฅฅ" : "status|db",
        "๐ โ GET LIST โ ๐": "nabilanavab",
        "๐ ADMIN ๐" : "status|admin",
        "๐ค USERS ๐ค" : "status|users",
        "ยซ BACK ยซ" : "Home|A"
    },
    "DB" : """๐ DATABASE :

**โ Database Users :** `{}` ๐
**โ Database Chats :** `{}` ๐""",
    "SERVER" : """**โ Total Space     :** `{}`
**โ Used Space     :** `{}({}%)`
**โ Free Space      :** `{}`
**โ CPU Usage      :** `{}`%
**โ RAM Usage     :** `{}`%
**โ Current Work  :** `{}`
**โ Message Id     :** `{}`""",
    "USERS" : "Users in Database are.",
    "NO_DB" : "No dataBASE set Yet ๐ฉ",
    "ADMIN" : "**Total ADMIN:** __{}__\n",
    "BACK" : { "ยซ BACK ยซ" : "status|home" },
    "HOME" : "`Now, select any option below to get current STATUS ๐ฑ.. `",
}

feedbackMsg = f"IF YOU โค THIS BOT, JOIN OUR [UPDATE CHANNEL]({settings.OWNED_CHANNEL}) TO STAY INFORMED.\n\n[Write a FEEDBACK ๐]({settings.FEEDBACK})"

# BANNED USER UI
BAN = {
    "UCantUse" : """Hey {}

FOR SOME REASON YOU CANT USE THIS BOT :(""",
    "UCantUseDB" : """Hey {}

FOR SOME REASON YOU CANT USE THIS BOT :(

REASON: {}""",
    "GroupCantUse" : """{} NEVER EXPECT A GOOD RESPONSE FROM ME

ADMINS RESTRICTED ME FROM WORKING HERE.. ๐คญ""",
    "GroupCantUseDB" : """{} NEVER EXPECT A GOOD RESPONSE FROM ME

ADMINS RESTRICTED ME FROM WORKING HERE.. ๐คญ

REASON: {}""",
    "cbNotU" : "Oops, Sorry to break your heart, this message is not for you ๐.\n\nBetter luck next time! ๐",
    "Fool" : "Please don't try to fool me.. ๐คญ",
    "banCB" : {
        "Create your Own Bot": f"{settings.SOURCE_CODE}",
        "Tutorial": f"{settings.SOURCE_CODE}",
        "Update Channel": "https://telegram.dog/ilovepdf_bot"
    },
    "Force" : """Wait [{}](tg://user?id={})..!!

Due To The Huge Traffic Only **Channel Members** Can Use this Bot ๐ถ

This Means That You Need To **Join** The Below Mentioned Channel for Using Me!

Hit on `"โป๏ธretryโป๏ธ"` after joining.. ๐""",
    "ForceCB" : {
        "๐ JOIN CHANNEL ๐" : "{0}",
        "โป๏ธ Refresh โป๏ธ" : "refresh{1}"
    },
}

checkPdf = {
    "pg" : "`Number of Pages: โข{}โข` ๐",
    "pdf" : """`What should I do with this file.?`

File Name : `{}`
File Size : `{}`""",
    "pdfCB1" : {
        "โญ METAยฃATA โญ" : "metaData",
        "๐ณ๏ธ PREVIEW ๐ณ๏ธ" : "preview",
        "๐ผ๏ธ IMAGES ๐ผ๏ธ" : "pdf|img",
        "โ๏ธ TEXT โ๏ธ" : "pdf|txt",
        "๐ ENCRYPT ๐" : "work|encrypt",
        "๐ DECRYPT ๐" : "work|decrypt",
        "๐๏ธ COMPRESS ๐๏ธ" : "work|compress",
        "๐คธ ROTATE ๐คธ" : "pdf|rotate",
        "โ๏ธ SPLIT โ๏ธ" : "pdf|split",
        "๐งฌ MERGE ๐งฌ" : "merge",
        "โข๏ธ STAMP โข๏ธ" : "pdf|stp",
        "โ๏ธ RENAME โ๏ธ" : "work|rename",
        "๐ URL ๐" : "link",
        "ยป ๐ดโโ ๏ธ MORE ๐ดโโ ๏ธ ยป" : "pdf2",
        "๐ซ CLOSE ๐ซ" : "close|all"
    },
    "pdfCB2" : {
        " โ SECOND PAGE  โ " : "nabilanavab",
        "๐ OCR ๐" : "work|ocr",
        "๐ฅท A4 FORMAT ๐ฅท" : "work|format", 
        "๐ค BLACK/WHITE ๐ค" : "baw",
        "๐ด SATUTATION ๐ด" : "sat",
        "๐ COMBINE PDF ๐" : "comb",
        "๐ ZOOM PDF ๐" : "zoom",
        "โ DELETE PAGES โ": "close|dev",
        "โ ADD PAGES โ" : "close|dev",
        "๐จ DRAW PDF ๐จ" : "draw",
        "๐ CODEC ๐" : "close|dev",
        "๐ฆ WATERMARK ๐ฆ" : "close|dev",
        "ยซ ๐ดโโ ๏ธ BACK ๐ดโโ ๏ธ ยซ" : "pdf1",
        "๐ซ CLOSE ๐ซ" : "close|all"
    },
    "error" : """__I can't do anything with this file.__ ๐

๐  `CODEC ERROR`  ๐""",
    "errorCB" : {
        "โ ERROR IN CODEC โ" : "error",
        "๐ธ CLOSE ๐ธ" : "close|all"
    },
    "encrypt" : """`FILE IS ENCRYPTED` ๐

File Name: `{}`
File Size: `{}`""",
    "encryptCB" : {"๐ DECRYPT ๐" : "work|decrypt"}
}

PROGRESS = {
    "progress" : """\n**Done โ : **{0}/{1}
**Speed ๐:** {2}/s
**Estimated Time โณ:** {3}""",
    "workInP" : "WORK IN PROGRESS.. ๐",
    "upFile" : "`Started Uploading..`๐ค",
    "refresh" : { "โป๏ธ Refresh โป๏ธ" : "{}" },
    "dlFile" : "`Downloading your file..` ๐ฅ",
    "dlImage" : "`Downloading your Image..โณ`",
    "upFileCB" : {"๐ค .. UPLOADING.. ๐ค" : "nabilanavab"},
    "takeTime" : """```โ๏ธ Work in Progress..`
`It might take some time..```๐""",
    "cbPRO_D" : ["๐ค DOWNLOAD: {:.2f}% ๐ค", "๐ฏ CANCEL ๐ฏ"],
    "cbPRO_U" : ["๐ค UPLOADED: {:.2f}% ๐ค", "๐ฏ CANCEL ๐ฏ"]
}

GENERATE = {
    "noQueue" : "`No Queue found..`๐ฒ",
    "noImages" : "No image found.!! ๐",
    "currDL" : "Downloaded {} Images ๐ฅฑ",
    "geting" : "File Name: `{}`\nPages: `{}`",
    "getFileNm" : "Now Send Me a File Name ๐: ",
    "deleteQueue" : "`Queue deleted Successfully..`๐คง",
    "getingCB" : {"๐ GENERATING PDF.." : "nabilanavab"},
}

document = {
    "reply" : checkPdf['pdf'],
    "upFile" : PROGRESS['upFile'],
    "process" : "โ๏ธ Processing..",
    "replyCB" : checkPdf['pdfCB1'],
    "inWork" : PROGRESS['workInP'],
    "download" : PROGRESS['dlFile'],
    "refresh" : PROGRESS['refresh'],
    "dlImage" : PROGRESS['dlImage'],
    "takeTime" : PROGRESS['takeTime'],
    "fromFile" : "`Converted: {} to {}`",
    "unsupport" : "Unsupported file..๐`",
    "cancelCB" : { "โจ Cancel โฉ" : "close|me" },
    "generate" : { "GENERATE ๐" : "generate" },
    "generateRN" : {
        "GENERATE ๐" : "generate",
        "RENAME โ๏ธ" : "generateREN"
    },
    "noAPI" : """`Please add convert API.. ๐ฉ

start ยป settings ยป api ยป add/change`""",
    "error" : """SOMETHING went WRONG.. ๐

ERROR: `{}`""",
    "setHdImg" : """Now Image To PDF is in HD mode ๐""",
    "setDefault" : { "ยซ Back to Default Quality ยซ" : "close|hd" },
    "useDOCKER" : "`File Not Supported, deploy bot using docker`",
    "big" : """Due to Overload, Owner limits {}mb for pdf files ๐

`please Send me a file less than {}mb Size` ๐""",
    "bigCB" : {
        "๐ Create 2Gb Support Bot ๐" : "https://github.com/nabilanavab/ilovepdf"
    },
    "imageAdded" : """`Added {} pages to your PDF..`๐ค

fileName: `{}.pdf`"""
}

gDocument = {
    "admin" : """Due to Some Telegram Limits..

I can only work as an admin
__Please promote me as admin__ โบ๏ธ""",
    "notDOC" : "Broh Please Reply to a Document or an Image..๐คง",
    "Gadmin" : """Only Group Admins Can Use This Bot
Else Come to my Pm ๐""",
    "adminO" : """`Only admins can do it..`

Or try on your pdfs(__reply to your message__)"""
}
gDocument.update(document)

noHelp = f"`No one gonna help you` ๐"

split = {
    "work" : ["Range", "Single"],
    "inWork" : PROGRESS['workInP'],
    "download" : PROGRESS['dlFile'],
    "cancelCB" : document['cancelCB'],
    "exit" : "`Process Cancelled..` ๐",
    "button" : {
        "โ๏ธ PDF ยป SPLIT โ" : "nabilanavab",
        "With In Range ๐ฆ" : "split|R",
        "Single Page ๐" : "split|S",
        "ยซ BACK ยซ" : "pdf1"
    },
    "over" : "`5 attempts over.. Process cancelled..`๐",
    "pyromodASK_1" : """__PDF Split ยป By Range
Now, Enter the range (start:end) :__

/exit __to cancel__""",
    "completed" : "`Downloading Completed..` โ",
    "error_1" : "`Syntax Error: justNeedStartAndEnd `๐ถ",
    "error_2" : "`Syntax Error: errorInEndingPageNumber `๐ถ",
    "error_3" : "`Syntax Error: errorInStartingPageNumber `๐ถ",
    "error_4" : "`Syntax Error: pageNumberMustBeADigit` ๐ง ",
    "error_5" : "`Syntax Error: noEndingPageNumber Or notADigit` ๐ถ",
    "error_6" : "`Can't find any number..`๐",
    "error_7" : "`Something went Wrong..`๐",
    "error_8" : "`Enter Numbers less than {}..`๐",
    "error_9" : "`1st Check Number of pages` ๐",
    "upload" : "โ๏ธ `Started Uploading..` ๐ค"
}

pdf2IMG = {
    "uploadfile" : split["upload"],
    "inWork" : PROGRESS['workInP'],
    "process" : document['process'],
    "download" : PROGRESS['dlFile'],
    "toImage" : {
        "โ๏ธ PDF ยป IMAGES โ" : "nabilanavab",
        "๐ผ IMG ๐ผ" : "pdf|img|img",
        "๐ DOC ๐" : "pdf|img|doc",
        "๐ค ZIP ๐ค" : "pdf|img|zip",
        "๐ฏ TAR ๐ฏ" : "pdf|img|tar",
        "ยซ BACK ยซ" : "pdf1" 
    },
    "imgRange" : {
        "โ๏ธ PDF ยป IMAGES ยป {} โ" : "nabilanavab",
        "๐ ALL ๐" : "p2img|{}A",
        "๐คง RANGE ๐คง" : "p2img|{}R",
        "๐ PAGES ๐" : "p2img|{}S",
        "ยซ BACK ยซ" : "pdf|img"
    },
    "over" : "`5 attempt over.. Process canceled..`๐",
    "pyromodASK_1" : """__Pdf - ImgโบDoc ยป Pages:
Now, Enter the range (start:end) :__

/exit __to cancel__""",
    "pyromodASK_2" : """"__Pdf - ImgโบDoc ยป Pages:
Now, Enter the Page Numbers seperated by__ (,) :

/exit __to cancel__""",
    "exit" : "`Process Canceled..` ๐",
    "error_1" : "`Syntax Error: justNeedStartAndEnd `๐ถ",
    "error_2" : "`Syntax Error: errorInEndingPageNumber `๐ถ",
    "error_3" : "`Syntax Error: errorInStartingPageNumber `๐ถ",
    "error_4" : "`Syntax Error: pageNumberMustBeADigit` ๐ง ",
    "error_5" : "`Syntax Error: noEndingPageNumber Or notADigit` ๐ถ",
    "error_6" : "`Can't find any number..`๐",
    "error_7" : "`Something went Wrong..`๐",
    "error_8" : "`PDF only have {} pages` ๐ฉ",
    "error_9" : "`1st Check Number of pages` ๐",
    "error_10" : "__Due to Some restrictions Bot Sends Only 50 pages as ZIP..__๐",
    "total" : "`Total pages: {}..โณ`",
    "upload" : "`Uploading: {}/{} pages.. ๐ฌ`",
    "current" : "`Converted: {}/{} pages.. ๐ค`",
    "complete" : "`Uploading Completed.. `๐๏ธ",
    "canceledAT" : "`Canceled at {}/{} pages..` ๐",
    "cbAns" : "โ๏ธ okDA, Canceling.. ",
    "cancelCB" : {"๐ค CANCEL ๐ค" : "close|P2I"},     # EDITABLE: โ
    "canceledCB" : {"๐ CANCELLED ๐" : "close|P2IDONE"},
    "completed" : {"๐ COMPLETED ๐" : "close|P2ICOMP"}
}

merge = {
    "inWork" : PROGRESS['workInP'],
    "process" : document['process'],
    "upload" : PROGRESS['upFile'],
    "load" : "__Due to Overload you can only merge 5 PDFs at a time__",
    "sizeLoad" : "`Due to Overload Bot Only Support %sMb PDFs..", # removing %s show error
    "pyromodASK" : """__MERGE pdfs ยป Total PDFs in queue: {}__

/exit __to cancel__
/merge __to merge__""",
    "exit" : "`Process Cancelled..` ๐",
    "total" : "`Total PDFs : {} ๐ก",
    "current" : "__Started Downloading PDF : {} ๐ฅ__",
    "cancel" : "`Merging Process Cancelled.. ๐`",
    "started" : "__Merging Started.. __ ๐ช",
    "caption" : "`Merged PDF ๐`",
    "error" : """`May be File Encrypted..`

Reason: {}"""
}

metaData = {
    "inWork" : PROGRESS['workInP'],
    "process" : document['process'],
    "download" : PROGRESS['dlFile'],   # [โ]
    "read" : "Please read this message again.. ๐ฅด"
}

preview = {
    "inWork" : PROGRESS['workInP'],
    "process" : document['process'],
    "error" : document['error'],
    "download" : PROGRESS['dlFile'],
    "_" : "PDF only have {} pages ๐ค\n\n",
    "__" : "PDF pages: {}\n\n",
    "total" : "`Total pages: {}..` ๐ค",
    "album" : "`Preparing an Album..` ๐คน",
    "upload" : f"`Uploading: preview pages.. ๐ฌ`"
}

stamp = {
    "stamp" : {
        "โ๏ธ PDF ยป STAMP โ" : "nabilanavab",
        "Not For Public Release ๐คง" : "pdf|stp|10",
        "For Public Release ๐ฅฑ" : "pdf|stp|8",
        "Confidential ๐คซ" : "pdf|stp|2",
        "Departmental ๐ค" : "pdf|stp|3",
        "Experimental ๐ฌ" : "pdf|stp|4",
        "Expired ๐" : "pdf|stp|5",
        "Final ๐ง" : "pdf|stp|6",
        "For Comment ๐ฏ๏ธ" : "pdf|stp|7",
        "Not Approved ๐" : "pdf|stp|9",
        "Approved ๐ฅณ" : "pdf|stp|0",
        "Sold โ" : "pdf|stp|11",
        "Top Secret ๐ท" : "pdf|stp|12",
        "Draft ๐" : "pdf|stp|13",
        "AsIs ๐ค" : "pdf|stp|1",
        "ยซ BACK ยซ" : "pdf1"
    },
    "stampA" : {
        "โ๏ธ PDF ยป STAMP ยป COLOR โ" : "nabilanavab",
        "Red โค๏ธ" : "spP|{}|r",
        "Blue ๐" : "spP|{}|b",
        "Green ๐" : "spP|{}|g",
        "Yellow ๐" : "spP|{}|c1",
        "Pink ๐" : "spP|{}|c2",
        "Hue ๐" : "spP|{}|c3",
        "White ๐ค" : "spP|{}|c4",
        "Black ๐ค" : "spP|{}|c5",
        "ยซ Back ยซ" : "pdf|stp"
    },
    "inWork" : PROGRESS['workInP'],
    "process" : document['process'],
    "download" : PROGRESS['dlFile'],
    "upload" : PROGRESS['upFile'],
    "stamping" : "`Started Stamping..` ๐ ",
    "caption" : """stamped pdf\ncolor : `{}`
annot : `{}`"""
}

work = {
    "inWork" : PROGRESS['workInP'],
    "process" : document['process'],
    "download" : PROGRESS['dlFile'],
    "takeTime" : PROGRESS['takeTime'],
    "upload" : PROGRESS['upFile'],
    "button" : document['cancelCB'],
    "rot360" : "You have some **big problem..๐**",
    "ocrError" : "Owner Restricted ๐๐ค",
    "largeNo" : "Send a PDF file less than 5 pages.. ๐",
    "pyromodASK_1" : """__PDF {} ยป
Now, please enter the PASSWORD :__

/exit __to cancel__""",
    "pyromodASK_2" : """__Rename PDF ยป
Now, please enter the NEW NAME:__

/exit __to cancel__""",
    "exit" : "`process canceled.. `๐",
    "ren_caption" : "__New Name:__ `{}`", 
    "notENCRYPTED" : "`File is Not Encrypted..` ๐",
    "compress" : """โ๏ธ ```Started Compressing.. ๐ก๏ธ
It might take some time..```๐""",
    "decrypt" : """โ๏ธ ```Started Decrypting.. ๐
It might take some time..```๐""",
    "encrypt" : """โ๏ธ ```Started Encrypting.. ๐
It might take some time..```๐""",
    "ocr" : """โ๏ธ ```Adding OCR Layer.. โ๏ธ
It might take some time..```๐""",
    "format" : """โ๏ธ ```Started Formatting.. ๐ค
It might take some time..```๐""",
    "rename" : """โ๏ธ ```Renameing PDf.. โ๏ธ
It might take some time..```๐""",
    "rot" : """โ๏ธ ```Rotating PDf.. ๐คธ
It might take some time..```๐""",
    "pdfTxt" : """โ๏ธ ```Extracting Text.. ๐พ
It might take some time..```๐""",
    "fileNm" : """Old Filename: {}
New Filename: {}""",
    "rotate" : {
        "โ๏ธ PDF ยป ROTATE โ" : "nabilanavab",
        "90ยฐ" : "work|rot90",
        "180ยฐ" : "work|rot180",
        "270ยฐ" : "work|rot270",
        "360ยฐ" : "work|rot360",
        "ยซ BACK ยซ" : "pdf1"
    },
    "txt" : {
        "โ๏ธ PDF ยป TXT โ" : "nabilanavab",
        "๐ MESSAGE ๐" : "work|M",
        "๐งพ TXT FILE ๐งพ" : "work|T",
        "๐ HTML ๐" : "work|H",
        "๐ JSON ๐" : "work|J",
        "ยซ BACK ยซ" : "pdf1"
    }
}

PROCESS = {
    "ocr" : "OCR added",
    "decryptError" : "__Cannot Decrypt the file with__ `{}` ๐ธ๏ธ",
    "decrypted" : "__Decrypted File__",
    "encrypted" : "__Page Number__: {}\n__key__ ๐: ||{}||",
    "compressed" : """`Original Size : {}
Compressed Size : {}

Ratio : {:.2f} %`""",
    "cantCompress" : "File Can't be Compressed More..๐ค",
    "pgNoError" : """__For Some Reason A4 FORMATTING Supports only for PDFs with less than 5 Pages__

Total Pages: {} โญ""",
    "ocrError" : "`Already Have A Text Layer.. `๐",
    "90" : "__Rotated 90ยฐ__",
    "180" : "__Rotated 180ยฐ__",
    "270" : "__Rotated 270ยฐ__",
    "formatted" : "A4 Formatted File",
    "M" : "โป Extracted {} Pages โป",
    "H" : "HTML File",
    "T" : "TXT File",
    "J" : "JSON File"
}

pdf2TXT = {
    "upload" : PROGRESS["upFile"],
    "exit" : split['exit'],
    "nothing" : "Nothing to create.. ๐",
    "TEXT" : "`Create PDF From Text Messages ยป`",
    "start" : "Started Converting txt to Pdf..๐",
    "font_btn" : {
        "TXT@PDF ยป SET FONT" : "nabilanavab",
        "Times" : "pdf|font|t",
        "Courier" : "pdf|font|c",
        "Helvetica (Default)" : "pdf|font|h",
        "Symbol" : "pdf|font|s",
        "Zapfdingbats" : "pdf|font|z",
        "๐ซ CLOSE ๐ซ" : "close|me"
    },
    "size_btn" : {
        "TXT@PDF ยป {} ยป SET SCALE" : "nabilanavab",
        "Portarate" : "t2p|{}|p",
        "Landscape" : "t2p|{}|l",
        "ยซ Back ยซ": "pdf|T2P"
    },
    "askT" : """__TEXT TO PDF ยป Now, please enter a TITLE:__

/exit __to cancel__\n/skip __to skip__""",
    "askC" : """__TEXT TO PDF ยป Now, please enter paragraph {}:__

/exit __to cancel__\n/create __to create__"""
}

URL = {
    "notPDF" : "`Not a PDF File",
    "close" : { "close" : "close|all" },
    "get" : {"๐งญ Get PDF File ๐งญ" : "getFile"},
    "error" : """๐ SOMETHING WENT WRONG ๐,

ERROR: `{}`

NB: In Groups, Bots Can Only fetch documents Send After Joining Group =)""",
    "done" : "```Almost Done.. โ\nNow, Started Uploading.. ๐ค```",
    "_error_" : "send me any url or direct telegram pdf links",
    "openCB" : {"Open In Browser" : "{}"},
    "_error" : "`Some Thing Went Wrong =(`\n\n`{}`",
    "_get" : """[Open Chat]({})

**ABOUT CHAT โ**
Chat Type   : {}
Chat Name : {}
Chat Usr    : @{}
Chat ID        : {}
Date : {}

**ABOUT MEDIA โ**
Media       : {}
File Name : {}
File Size   : {}
File Type : {}"""
}

getFILE = {
    "wait" : "Wait.. Let me.. ๐",
    "inWork" : PROGRESS['workInP'],
    "big" : "Send PDF url less than {}mb",
    "dl" : {"๐ฅ ..DOWNLOADING.. ๐ฅ" : "nabilanavab"},
    "up" : {"๐ค ..UPLOADING..  ๐ค" : "nabilanavab"},
    "complete" : {"๐ COMPLETED ๐" : f"{str(settings.SOURCE_CODE)}"}
}

cbAns = [
    "This feature is Under Development โท๏ธ",
    "Error annenn paranjille.. then what.. ๐",
    "Process Canceled.. ๐",
    "File Not Encrypted.. ๐",
    "Nothing Official About it.. ๐",
    "๐ Completed.. ๐"
]

wa = {
    "exit" : split["exit"],
    "over" : pdf2IMG['over'],
    "upFile" : PROGRESS['upFile'],
    "inWork" : PROGRESS['workInP'],
    "process" : document['process'],
    "download" : PROGRESS['dlFile'],
    "error" : "Something went Wrong ๐",
    "cancelCB" : {"โจ Cancel โฉ" : "close|me"},
    "add" : "Adding watermark to PDF File ๐ฉ",
    "waDL" : "__Getting watermark File..__ ๐",
    "type" : {
        "โ๏ธ PDF ยป WATERMARK โ" : "nabilanavab",
        "TEXT" : "pdf|wa|txt",
        "IMAGE" : "pdf|wa|img",
        "PDF" : "pdf|wa|pdf",
        "ยซ BACK ยซ" : "pdf2"
    },
    "op" : {
        "โ๏ธ PDF ยป WATERMARK ยป {} ยป OPCACiTY โ" : "nabilanavab",
        "10 %":"pdf|wa|{}|o01",
        "20 %":"pdf|wa|{}|o02",
        "30 %":"pdf|wa|{}|o03",
        "40 %":"pdf|wa|{}|o04",
        "50 %":"pdf|wa|{}|o05",
        "60 %":"pdf|wa|{}|o06",
        "70 %":"pdf|wa|{}|o07",
        "80 %":"pdf|wa|{}|o08",
        "90 %":"pdf|wa|{}|o09",
        "100 %":"pdf|wa|{}|o10",
        "ยซ BACK ยซ" : "pdf|wa"
    },
    "po" : {
        "โ๏ธ PDF ยป WATERMARK ยป POSiTiON โ" : "nabilanavab",
        "แ แ แ  " : "wa|{0}|{1}|TL",
        "แ แ โฏ โฏ" : "wa|{0}|{1}|TM",
        "แ แ โ" : "wa|{0}|{1}|TR",
        "แ แ โโ" : "wa|{0}|{1}|ML",
        "แ แ ใ" : "wa|{0}|{1}|MM",
        "แ แ โ  โ " : "wa|{0}|{1}|MR",
        "แ แ โ" : "wa|{0}|{1}|BL",
        "แ โแ โ" : "wa|{0}|{1}|BM",
        "แ โ แ โ" : "wa|{0}|{1}|BR",
        "ยซ BACK ยซ" : "pdf|wa|{0}"
    }, 
    "txt" : """__Now, Send me any Text Message__

/exit : to cancel""", 
    "pdf" : """__Send me the watermark pdf.__

/exit : to cancel""",
    "img" : """__Send me the watermark Image as file.__
__ Supported Files [png, jpeg, jpg]__

/exit : to cancel""",
}

comb = {
    "upFile" : PROGRESS['upFile'],
    "inWork" : PROGRESS['workInP'],
    "process" : document['process'],
    "process" : document['process'],
    "download" : PROGRESS['dlFile'],
    "cancelCB" : {"โจ Cancel โฉ" : "close|me"},
}

inline_query = {
    "capt" : "SET LANGUAGE โ๏ธ",
    "des" : "By: @nabilanavab โค",
    "TOP" : { "Now, Select Language โฎท" : "nabilanavab" },
}

LINK = {
    "gen" : "`๐ Generating..`",
    "_gen" : """```๐ Generating..
We're working on it!

Please allow a moment for the processing to complete.```""",
    "no" : "Unfortunately, we encountered an error ๐",
    "type" : """`๐ Generating..`

**Public** ๐ข:
__The file accessed via this link will be publicly available, allowing anyone to save and forward it__.


**Protect** ๐:
__Ensures the confidentiality of the message by preventing its forwarding and saving__.""",
    "notify" : "Get Notify when a someone fetch this pdf",
    "notify_pvt" : {
        "๐ NOTIFY ๐" : "link-pvt-ntf",
        "๐ MUTE ๐" : "link-pvt-mut"
    },
    "notify_pub" : {
        "๐ NOTIFY ๐" : "link-pbc-ntf",
        "๐ MUTE ๐" : "link-pbc-mut"
    },
    "typeBTN" : {
        "๐ข PUBLIC ๐ข" : "link-pub",
        "๐ PRIVATE ๐" : "link-pvt"
    },
    "link" : "**Here it is! This is what you were searching for..**",
    "error" : "Oops, it looks like something went wrong. Please try again later.\n\n`ERROR:` {}"
}

DELETE = {
    "button" : {
        "โ๏ธ PDF ยป SPLIT โ" : "nabilanavab",
        "With In Range ๐ฆ" : "split|dR",
        "Single Page ๐" : "split|dS",
        "ยซ BACK ยซ" : "pdf1"
    },
}
