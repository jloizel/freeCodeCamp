const textInput = document.getElementById("text-input");
const checkBtn = document.getElementById("check-btn");
var result = document.getElementById("result");

function palindrome(text) {
  if (text === "") {
    return false;
  }

  const textClean = text.replace((/[^a-zA-Z0-9]/g), '').toLowerCase();
  return palindromeChecker(textClean);
}

const palindromeChecker = (text) => {
  var textArray = text.split('');
  if (textArray.length == 1) {
    return true;
  } else if (textArray.length === 2 && textArray[0] === textArray[1]) {
    return true;
  } else if (textArray.length > 2 && textArray[0] === textArray[textArray.length - 1]) {
    textArray.shift();
    textArray.pop();
    var shortenedText = textArray.join('');
    return palindromeChecker(shortenedText) ? true : false;
  } else {
    return false;
  }
}

checkBtn.addEventListener("click", (e) => {
  e.preventDefault();
  if (textInput.value === "") {
    alert("Please input a value");
  } else if (palindrome(textInput.value)) {
    result.innerHTML = `
    <p><strong>${textInput.value}</strong> is a palindrome.</p>
    `
  } else {
    result.innerHTML = `
    <p><strong>${textInput.value}</strong> is not a palindrome.</p>`
  };
});