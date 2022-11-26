const step = 4; //1ページの表示数
let total_Pages = Math.floor(channels.length / step) + 1; //総ページ数
let current_Page = 1; //現在のページ

//ページネーション
const make_Pagenation = (total_Pages) => {
  const pagenation_Ul = document.getElementById("pagination");
  //ulを空に
  pagenation_Ul.innerHTML = "";
  //pagenationの要素作成
  for (let num = 1; num <= total_Pages; num++) {
    const pagination_Li = document.createElement("li");
    pagination_Li.textContent = num;
    pagination_Li.addEventListener("click", () => {
      make_Chatroom_List(num, step);
    });
    pagenation_Ul.appendChild(pagination_Li);
  }
};

//現在表示されてるページの背景塗りつぶし

//チャットルームリストを表示
const make_Chatroom_List = (page, step) => {
  const first_Room = (page - 1) * step + 1; //現在のページの最初のルーム
  const end_Room = page * step; //現在のページの最後のルーム
  const room_Ul = document.getElementById("roomlist");
  //ulを空に
  room_Ul.innerHTML = "";
  channels.forEach((channel, index) => {
    if (index < first_Room - 1 || index > end_Room - 1) return;
    const room_Li = document.createElement("li");
    const room_Anchor = document.createElement("a");
    const url = `/detail/${channel.id}`;
    room_Anchor.innerText = channel.name;
    room_Anchor.setAttribute("href", url);
    room_Li.appendChild(room_Anchor);
    room_Ul.appendChild(room_Li);
  });
};

//ページネーションの次へと前えへ機能
document.getElementById("next").addEventListener("click", () => {
  if (current_Page >= total_Pages) return;
  current_Page += 1;
  make_Chatroom_List(current_Page, step);
});

document.getElementById("prev").addEventListener("click", () => {
  if (current_Page === 1) return;
  current_Page -= 1;
  make_Chatroom_List(current_Page, step);
});

//ページをロードした時
window.onload = () => {
  make_Pagenation(total_Pages);
  make_Chatroom_List(current_Page, step);
};
