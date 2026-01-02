console.log(
    "===========================================================STRING==========================================================="
);

const string4 = new String("A String object");

// ChartAt()
const mtChartAt = string4.charAt(0); // --> "A"
const mtChartAtVer1 = string4[0]; // --> "A"

// lastIndexOf() --> vị trí xuất hiện cuối cùng
const mtLastIndexOf = string4.lastIndexOf("t", 12);

// InCludes
const mtIncludes = string4.includes("String"); // -->  true

// Start With
const mtStartWidth = string4.startsWith("S", 2); // --> true

// End With
const mtEndWith = string4.endsWith("object"); // --> true

// Slice
const mtSlice = string4.slice(8); //  --> object

// SubString giống Slice nhưng không nhận số âm
const mtSubString = string4.substring(8);

// Replace
const mtReplace = string4.replace("String", "number"); //--> A Number object

// ReplaceAll
const mtReplaceAll = string4.replaceAll("t", "N"); // --> A SNring  objecN

// Split
const mtSplit = string4.split("t"); // --> [ 'A S', 'ring objec', '' ]

// Concat
const mtConcat = string4.concat("_text to concat"); // --> A String object_text to concat

// Trim
const mtTrim = "    i leanning javascirpt    ".trim(); // -> i leanning javascirpt

// Repeat
const mtRepeat = string4.repeat(1);

// CharCodeAt
const mtCharCodeAt = string4.charCodeAt(1);

// 

