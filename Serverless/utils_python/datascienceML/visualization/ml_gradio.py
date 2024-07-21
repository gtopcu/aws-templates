
import gradio as gr

demo = gr.Interface(
    fn=soru_cevap,
    inputs=[
        gr.Textbox(lines=5, placeholder="Siparişinizle ilgili sorunuzu buraya girebilirsiniz. ")
    ],
    outputs=gr.Textbox(label="Müşteri hizmetleri cevabı:"),
    title="Byson Müşteri Hizmetleri Hattı",
    description="Byson Müşteri Hizmetleri Hattı'na Dilediğiniz Soruyu Sorabilirsiniz. "
)

demo.launch(debug=True)