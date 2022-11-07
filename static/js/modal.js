// モーダルを表示させる

const addChannelModal = document.getElementById("btn-create-room");
const deleteChannelModal = document.getElementById("delete-channel-modal");

const addPageButtonClose = document.getElementById("add-page-close-btn");
const deletePageButtonClose = document.getElementById("delete-page-close-btn");

const addChannelBtn = document.getElementById("btn-create-room");

const addChannelConfirmBtn = document.getElementById(
  "add-channel-confirmation-btn"
);
const deleteChannelConfirmBtn = document.getElementById(
  "delete-channel-confirmation-btn"
);

// モーダルを開く
// <button id="btn-create-room">チャンネル追加</button>ボタンがクリックされた時
addChannelBtn.addEventListener("click", () => {
  modalOpen("add");
});

function modalOpen(mode) {
  if (mode === "add") {
    addChannelModal.style.display = "block";
    console.log("add来てるよ");
  } else if (mode === "delete") {
    deleteChannelModal.style.display = "block";
  } else if (mode === "update") {
    updateChannelModal.style.display = "block";
  }
}

// モーダル内のバツ印がクリックされた時
//addPageButtonClose.addEventListener("click", () => {
//  modalClose("add");
//});
//deletePageButtonClose.addEventListener("click", () => {
//  modalClose("delete");
//});
//
//function modalClose(mode) {
//  if (mode === "add") {
//    addChannelModal.style.display = "none";
//  } else if (mode === "delete") {
//    deleteChannelModal.style.display = "none";
//  } else if (mode === "update") {
//    updateChannelModal.style.display = "none";
//  }
//}
//
//// モーダルコンテンツ以外がクリックされた時
//addEventListener("click", outsideClose);
//function outsideClose(e) {
//  if (e.target == addChannelModal) {
//    addChannelModal.style.display = "none";
//  } else if (e.target == deleteChannelModal) {
//    deleteChannelModal.style.display = "none";
//  }
//}
