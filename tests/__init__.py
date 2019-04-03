import os


test_data_dir = os.path.join(os.path.dirname(__file__), 'data')
# pdf_name = 'plan_l.pdf'
# pdf_name = 'plan_p.pdf'
# pdf_name = 'article.pdf'
# pdf_name = 'con docs2.pdf'
img_name = 'floor plan.png'
img_path = os.path.join(test_data_dir, img_name)
wtr_name = 'watermark.png'
wtr_path = os.path.join(test_data_dir, wtr_name)


__all__ = ['img_path', 'wtr_path', 'test_data_dir']
