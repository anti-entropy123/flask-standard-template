from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class OneForm(FlaskForm):
    name = StringField(
        '你的名字是',                   # 表单字段的label 
        validators=[DataRequired()]    # 此字段内容不能为空
        )
    submit = SubmitField('提交')