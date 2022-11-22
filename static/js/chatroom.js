// ページ読み込み時に自動で下までスクロールする
window.onload = () => {
  const elm = document.documentElement;

  // scrollHeight ページの高さ clientHeight ブラウザの高さ
  const bottom = elm.scrollHeight - elm.clientHeight;
  window.scroll(0, bottom);
};
