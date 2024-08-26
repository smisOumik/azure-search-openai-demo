import React from 'react';
import Example from './Example';
import styles from './Example-module.css';

const templates = [
  "記載ルール: テンプレートをコピーして貼り付け、必要事項を編集してください。「」の部分のみ修正すること。編集後「」を削除すること。改行を入れないでください。",
  "以下コピーしてください。<br> # リクエスト <br> - 「システム名を記載」に関する問合せがきました。「聞きたいことを記載」。",
  "以下コピーしてリクエストの下にペストして記入してください。 <br> # 問合せの情報 <br> - 発生箇所: 「箇所を記載」 <br> トリガ: 「事象が発生した際のきっかけとなった操作などを記載」 <br> 事象詳細: 「詳細を記載」 <br> エラーメッセージ: 「エラーメッセージを記載」"
];

const ExampleList: React.FC = () => {
  return (
    <ul className={styles.examplesNavList}>
      {templates.map((template, i) => (
        <li key={i}>
          <Example text={template} />
        </li>
      ))}
    </ul>
  );
};

export default ExampleList;