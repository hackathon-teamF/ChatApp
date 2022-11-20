// ページ読み込み時に自動で下までスクロールする

window.onload = () => {
  const elm = document.getElementById("message-container");
  elmHeight = elm.scrollHeight;
  elm.scrollTop = elmHeight;
};
