# RapidOcr-Paragraphizer

![Views](https://komarev.com/ghpvc/?username=llap4585&repo=RapidOcr-Paragraphizer&label=Project%20Views&color=blue&style=flat-square)


[English](#english) | [中文](#chinese)

機械翻訳 | Maschinelle Übersetzung | Traduction automatique | Traducción Automática | मशीनी अनुवाद

[日本語](#japanese) | [Deutsch](#deutsch) | [Français](#francais) | [Español](#espanol) | [हिन्दी](#hindi)

---

<a name="english"></a>
## English

**RapidOCR-Paragraphizer** is an OCR post-processing tool born from the need to handle **scanned medical report PDFs** (PDF splitting functionality is not provided; PyMuPDF is recommended). It focuses on paragraph-level structural reconstruction of RapidOCR recognition results.

By analyzing the layout and structural features of the OCR output, this project automatically integrates discrete text lines into semantically coherent paragraphs, improving the usability of medical texts for reading, searching, API calls, and subsequent NLP tasks.

⚠️ **Limitations:**

This project uses a layout-based approach for paragraph reconstruction. Due to significant variations in scanned documents regarding layout, fonts, and line spacing, **this algorithm may not perform consistently across all document formats.**

The current solution aims to provide an **interpretable, adjustable, and controllable baseline** for paragraph reconstruction, serving as a reference for more complex layout modeling or machine learning methods.

In practice, some parameters may need fine-tuning based on specific document types, such as:
* `indent_threshold`: Threshold for determining paragraph indentation.
* `line_gap_threshold`: Threshold for distinguishing line breaks from paragraph spacing.

Additionally, output effects can be optimized by adjusting the string concatenation logic based on document format:
`txts[i]= '\n' + str(txts[i]) +'\n'` or `txts[i]= '\n' +str(txts[i])`

---

<a name="chinese"></a>
## 中文
**RapidOCR-Paragraphizer** 是一款诞生于 **医学报告扫描PDF**的 OCR 后处理工具（未提供PDF拆分功能，推荐使用PyMuPDF），
专注于对 RapidOCR 识别结果进行段落级结构重建。

该项目通过分析 OCR 输出中的版式与布局特征，将原本离散的文本行自动整合为语义连贯的段落，
以提升医学文本在阅读、检索、API 调用及后续自然语言处理场景中的可用性。

⚠️ **限制：**

本项目采用基于版式特征的方法对 OCR 输出进行段落重建。
由于扫描文档在排版、字体和行距等方面存在较大差异， **该算法并非在所有文档格式下都能稳定工作。**

当前方案旨在提供一个 **可解释、可调、可控的段落重建基线**，
可作为后续更复杂布局建模或学习方法的参考。

在实际使用中，部分参数需要根据具体文档类型进行微调，例如：

* `indent_threshold`：用于判断段落缩进的阈值
* `line_gap_threshold`：用于区分行内换行与段落间距

以及基于文档格式不同可以替换来达到更好的输出效果：

`txts[i]= '\n' + str(txts[i]) +'\n'` 或 `txts[i]= '\n' +str(txts[i])`

---

<a name="japanese"></a>
## 日本語 (機械翻訳)

**RapidOCR-Paragraphizer** は、**医療報告書のスキャンPDF**（PDF分割機能は含まれていません。PyMuPDFを推奨します）から生まれたOCR後処理ツールです。RapidOCRの認識結果に対して、段落レベルの構造再構成を行うことに特化しています。

このプロジェクトは、OCR出力のレイアウトと構成の特徴を分析することで、本来離散的なテキスト行を意味的に首尾一貫した段落に自動的に統合し、閲覧、検索、API呼び出し、およびその後の自然言語処理における医療テキストの使いやすさを向上させます。

⚠️ **制限事項：**

本プロジェクトは、レイアウト特徴に基づいた手法でOCR出力の段落再構成を行います。スキャンされたドキュメントはレイアウト、フォント、行間などが大きく異なるため、**このアルゴリズムはすべてのドキュメント形式で安定して動作するわけではありません。**

現在のソリューションは、**解釈可能で、調整可能、かつ制御可能な段落再構成のベースライン**を提供することを目的としており、より複雑なレイアウトモデリングや学習手法の参考として活用いただけます。

実際の使用において、一部のパラメータは特定のドキュメントタイプに合わせて微調整が必要です。例：
* `indent_threshold`: 段落のインデントを判定するための閾値
* `line_gap_threshold`: 行内の改行と段落間の間隔を区別するための閾値

また、ドキュメント形式に応じて、より良い出力結果を得るために以下の処理を差し替えることが可能です：
`txts[i]= '\n' + str(txts[i]) +'\n'` または `txts[i]= '\n' +str(txts[i])`

---

<a name="deutsch"></a>
## Deutsch (Maschinelle Übersetzung)

**RapidOCR-Paragraphizer** ist ein OCR-Postprocessing-Tool, das für die Verarbeitung von **gescannten medizinischen Berichten im PDF-Format** entwickelt wurde (eine PDF-Splitting-Funktion ist nicht enthalten; PyMuPDF wird empfohlen). Der Fokus liegt auf der Rekonstruktion der Absatzstruktur aus RapidOCR-Ergebnissen.

Durch die Analyse von Layout-Merkmalen in der OCR-Ausgabe führt dieses Projekt ursprünglich diskrete Textzeilen automatisch zu semantisch kohärenten Absätzen zusammen. Dies verbessert die Nutzbarkeit medizinischer Texte für das Lesen, Suchen, API-Aufrufe und die nachfolgende NLP-Verarbeitung.

⚠️ **Einschränkungen:**

Dieses Projekt verwendet einen layoutbasierten Ansatz zur Absatzrekonstruktion. Da gescannte Dokumente erhebliche Unterschiede in Layout, Schriftarten und Zeilenabständen aufweisen, **arbeitet dieser Algorithmus nicht bei allen Dokumentformaten stabil.**

Die aktuelle Lösung zielt darauf ab, eine **interpretierbare, anpassbare und kontrollierbare Baseline** für die Absatzrekonstruktion bereitzustellen, die als Referenz für komplexere Layout-Modellierungen oder Lernverfahren dienen kann.

In der Praxis müssen einige Parameter je nach Dokumenttyp feinjustiert werden, zum Beispiel:
* `indent_threshold`: Schwellenwert zur Bestimmung von Einzügen.
* `line_gap_threshold`: Schwellenwert zur Unterscheidung zwischen Zeilenumbrüchen und Absatzabständen.

Zudem kann die Ausgabe je nach Format optimiert werden:
`txts[i]= '\n' + str(txts[i]) +'\n'` oder `txts[i]= '\n' +str(txts[i])`

---

<a name="francais"></a>
## Français (Traduction Automatique)

**RapidOCR-Paragraphizer** est un outil de post-traitement OCR conçu pour les **rapports médicaux scannés en PDF** (la fonction de découpage PDF n'est pas fournie ; PyMuPDF est recommandé). Il se concentre sur la reconstruction structurelle au niveau des paragraphes des résultats de RapidOCR.

En analysant les caractéristiques de mise en page de la sortie OCR, ce projet intègre automatiquement des lignes de texte initialement discrètes en paragraphes sémantiquement cohérents, afin d'améliorer l'utilisabilité des textes médicaux pour la lecture, la recherche, les appels API et le traitement automatique du langage naturel (TALN).

⚠️ **Limitations :**

Ce projet utilise une méthode basée sur les caractéristiques de mise en page pour la reconstruction des paragraphes. En raison des variations importantes des documents scannés (mise en page, polices, interlignage), **cet algorithme ne fonctionne pas de manière stable sur tous les formats de documents.**

La solution actuelle vise à fournir une **base de référence interprétable, ajustable et contrôlable** pour la reconstruction de paragraphes, pouvant servir de point d'appui à des méthodes de modélisation de mise en page plus complexes.

En pratique, certains paramètres doivent être ajustés selon le type de document, par exemple :
* `indent_threshold` : Seuil pour juger de l'alinéa d'un paragraphe.
* `line_gap_threshold` : Seuil pour distinguer un simple retour à la ligne d'un espacement entre paragraphes.

De plus, selon le format du document, vous pouvez modifier la concaténation pour un meilleur rendu :
`txts[i]= '\n' + str(txts[i]) +'\n'` ou `txts[i]= '\n' +str(txts[i])`

---

<a name="espanol"></a>
## Español (Traducción Automática)

**RapidOCR-Paragraphizer** es una herramienta de post-procesamiento OCR nacida de la necesidad de manejar **informes médicos escaneados en PDF** (la función de división de PDF no está incluida; se recomienda PyMuPDF). Se centra en la reconstrucción estructural a nivel de párrafo de los resultados de reconocimiento de RapidOCR.

Mediante el análisis de las características de diseño y disposición de la salida de OCR, este proyecto integra automáticamente líneas de texto discretas en párrafos semánticamente coherentes, mejorando la utilidad de los textos médicos para lectura, búsqueda, llamadas a API y procesamiento de lenguaje natural (NLP).

⚠️ **Limitaciones:**

Este proyecto utiliza un enfoque basado en el diseño para la reconstrucción de párrafos. Debido a las grandes diferencias en los documentos escaneados en cuanto a diseño, fuentes y espaciado de líneas, **este algoritmo no funciona de manera estable en todos los formatos de documentos.**

La solución actual tiene como objetivo proporcionar una **línea base interpretable, ajustable y controlable** para la reconstrucción de párrafos, que puede servir como referencia para métodos de aprendizaje o modelado de diseño más complejos.

En el uso práctico, algunos parámetros requieren ajustes finos según el tipo de documento, por ejemplo:
* `indent_threshold`: Umbral para determinar la sangría del párrafo.
* `line_gap_threshold`: Umbral para distinguir entre saltos de línea y espaciado de párrafo.

Además, el efecto de salida se puede optimizar según el formato del documento cambiando:
`txts[i]= '\n' + str(txts[i]) +'\n'` o `txts[i]= '\n' +str(txts[i])`

---

<a name="hindi"></a>
## हिन्दी (मशीनी अनुवाद)

**RapidOCR-Paragraphizer** एक OCR पोस्ट-प्रोसेसिंग टुल है जिसे **स्कैन की गई मेडिकल रिपोर्ट PDF** (PDF विभाजन सुविधा उपलब्ध नहीं है; PyMuPDF की अनुशंसा की जाती है) के लिए बनाया गया है। यह RapidOCR पहचान परिणामों के पैराग्राफ-स्तरीय संरचनात्मक पुनर्निर्माण पर केंद्रित है।

यह प्रोजेक्ट OCR आउटपुट की लेआउट और संरचनात्मक विशेषताओं का विश्लेषण करके, अलग-अलग टेक्स्ट लाइनों को स्वचालित रूप से अर्थपूर्ण पैराग्राफ में जोड़ता है। इसका उद्देश्य पढ़ने, खोजने, API कॉल और बाद के NLP कार्यों में मेडिकल टेक्स्ट की उपयोगिता को बढ़ाना है।

⚠️ **सीमाएं:**

यह प्रोजेक्ट पैराग्राफ पुनर्निर्माण के लिए लेआउट-आधारित पद्धति का उपयोग करता है। स्कैन किए गए दस्तावेज़ों के लेआउट, फ़ॉन्ट और लाइन स्पेसिंग में बहुत अंतर होने के कारण, **यह एल्गोरिदम सभी दस्तावेज़ प्रारूपों पर स्थिर रूप से काम नहीं कर सकता है।**

वर्तमान समाधान का उद्देश्य पैराग्राफ पुनर्निर्माण के लिए एक **व्याख्या योग्य, समायोज्य और नियंत्रणीय आधार रेखा (baseline)** प्रदान करना है, जिसे भविष्य के जटिल लेआउट मॉडलिंग या सीखने के तरीकों के लिए संदर्भ के रूप में उपयोग किया जा सकता है।

व्यावहारिक उपयोग में, विशिष्ट दस्तावेज़ प्रकारों के आधार पर कुछ मापदंडों (parameters) को ठीक करने की आवश्यकता हो सकती है, जैसे:
* `indent_threshold`: पैराग्राफ इंडेंटेशन निर्धारित करने के लिए थ्रेशोल्ड।
* `line_gap_threshold`: लाइनों के बीच के अंतर और पैराग्राफ के बीच के अंतर को पहचानने के लिए थ्रेशोल्ड।

इसके अलावा, दस्तावेज़ प्रारूप के आधार पर बेहतर आउटपुट प्राप्त करने के लिए इसे बदला जा सकता है:
`txts[i]= '\n' + str(txts[i]) +'\n'` या `txts[i]= '\n' +str(txts[i])`

---

## 🛡️ Privacy & Security

**Local Processing Only:** This tool performs all operations locally on your machine. No medical reports, patient data, or sensitive information are uploaded to any external servers or cloud services. Your data remains under your control at all times.

**Third-party Disclaimer:** All third-party libraries required for operation are provided by the user's environment. These dependencies and their components are not under the management or control of this project.

**仅限本地处理：** 本工具的所有操作均在您的本地计算机上执行。不会将任何医疗报告、患者数据或敏感信息上传到任何外部服务器或云服务。您的数据始终由您掌控。

**第三方库声明：** 本工具运行所依赖的所有第三方库均由用户环境提供，这些第三方库及其相关组件不在本项目的管理与控制范围内。

---

## 🛠️ Requirements

```text
opencv-python
numpy
rapidocr_onnxruntime
```
---

## 💪References / Citation
```markdown
This project builds upon the RapidOCR toolbox. If you use RapidOCR, please cite:

@misc{RapidOCR2021,
    title={{Rapid OCR}: OCR Toolbox},
    author={RapidAI Team},
    howpublished = {\url{https://github.com/RapidAI/RapidOCR}},
    year={2021}
}

If you use this project, please cite it as:

@misc{llap4585,
    title={{RapidOcr-Paragraphizer}: Automatically merges scanned text into semantically linked paragraphs.},
    author={llap4585},
    howpublished = {\url{https://github.com/llap4585/RapidOcr-Paragraphizer}},
    year={2026}
}
```
---

> **Disclaimer:** The non-English and non-Chinese versions of this documentation are provided for convenience only and were generated using machine translation. In case of any discrepancy, the Chinese version shall prevail.
