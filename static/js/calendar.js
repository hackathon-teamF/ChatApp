const date = new Date(); // 現在時刻
const year = date.getFullYear();
const month = date.getMonth() + 1;
const weeks = ["日", "月", "火", "水", "木", "金", "土"];
const month_Start = new Date(year, month - 1, 1); // 月の最初の日を取得
const month_End = new Date(year, month, 0); // 月の最後の日を取得
const end_Day = month_End.getDate(); // 月の末日
const start_Day = month_Start.getDay(); // 月の最初の日の曜日を取得 weeksのindex番号
let dayCount = 1; // 日にちのカウント
let calendarHtml = ""; // htmlのテーブル作成用

calendarHtml += "<h1>" + year + "/" + month + "</h1>";
calendarHtml += "<table>";

// 曜日の行を作成
for (let week = 0; week < weeks.length; week++) {
  calendarHtml += "<th>" + weeks[week] + "</th>";
}

//カレンダー全体の行作成
for (let w = 0; w < 6; w++) {
  calendarHtml += "<tr>";

  //カレンダー全体の列作成
  for (let d = 0; d < 7; d++) {
    //月初よりも前の場合
    if (w == 0 && d < start_Day) {
      calendarHtml += "<td></td>";
      //月末よりも後の場合
    } else if (dayCount > end_Day) {
      calendarHtml += "<td></td>";
    } else {
      calendarHtml += "<td>" + dayCount + "</td>";
      dayCount++;
    }
  }
  calendarHtml += "</tr>";
}
calendarHtml += "</table>";

document.querySelector("#calendar").innerHTML = calendarHtml;
