// ボクセラミングのライブラリをインポートします
// npm install voxelamming

// スクリプトを起動する
// node javascriptSample.mjs

import { Voxelamming } from 'voxelamming';

const roomName = '1000';
const vox = new Voxelamming(roomName);

vox.setBoxSize(0.5);

for (let i = 0; i < 100; i++) {
  vox.createBox(-1, i, 0, 0, 1, 1);
  vox.createBox(0, i, 0, 1, 0, 0);
  vox.createBox(1, i, 0, 1, 1, 0);
  vox.createBox(2, i, 0, 0, 1, 1);
}

for (let i = 0; i < 50; i++) {
  vox.removeBox(0, i * 2, 0);
  vox.removeBox(1, i * 2 + 1, 0);
}

await vox.sendData("main");
console.log('send data done')
