🛒 2. ビジョンベースの簡単決済キオスク
📄 概要
デジタル疎外層（高齢者層）のために、商品の自動認識と簡単決済機能を提供するキオスクプロジェクトです。複雑な操作なしに商品を置くとAIが認識し、カードをタグ付けして決済します。

🙋‍♀️ 担当役割 (1): NFC簡単決済モジュールの開発 (C++)
主な機能:

pn532 NFCシールドを制御し、カード固有ID(UID)をタグ付けするC++コードをArduino環境で作成。

Arduino UNOで認識したカード情報をAWSサーバーに転送。

使用技術:

HW: Arduino UNO R3, pn532 NFC/RFID シールド

SW: C++, AWS

🙋‍♀️ 担当役割 (2): AI商品認識モデルの学習 (YOLO)
主な機能:

Roboflowツールを使用して実際の商品画像を収集・ラベリングし、カスタムデータセットを構築。

YOLOv8モデルをPyTorchベースのGPU環境で学習させ、モデル性能(mAP, Precision/Recall)を分析およびチューニング。

学習済みモデル(best.pt)をRaspberry Pi 5にデプロイし、リアルタイムカメラ(Pi Camera Module 3)映像から商品を推論(Inference)。

使用技術:

HW: Raspberry Pi 5, Raspberry Pi Camera Module 3

SW: Python, YOLOv8, Roboflow, PyTorch
