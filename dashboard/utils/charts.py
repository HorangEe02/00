import plotly.express as px
import pandas as pd


def create_sales_trend_chart(df: pd.DataFrame) -> px.line:
    """월별 매출 추이 라인 차트"""
    monthly = (
        df.groupby(df['date'].dt.to_period('M'))['sales']
        .sum()
        .reset_index()
    )
    monthly['date'] = monthly['date'].dt.to_timestamp()

    fig = px.line(
        monthly,
        x='date',
        y='sales',
        title='월별 매출 추이',
        labels={'date': '월', 'sales': '매출(원)'},
        markers=True,
    )
    fig.update_layout(height=400)
    return fig


def create_product_bar_chart(df: pd.DataFrame) -> px.bar:
    """제품별 매출 막대 차트"""
    by_product = (
        df.groupby('product')['sales']
        .sum()
        .reset_index()
        .sort_values('sales', ascending=False)
    )

    fig = px.bar(
        by_product,
        x='product',
        y='sales',
        title='제품별 매출',
        labels={'product': '제품', 'sales': '매출(원)'},
        color='product',
    )
    fig.update_layout(height=400, showlegend=False)
    return fig


def create_region_pie_chart(df: pd.DataFrame) -> px.pie:
    """지역별 매출 파이 차트"""
    by_region = (
        df.groupby('region')['sales']
        .sum()
        .reset_index()
    )

    fig = px.pie(
        by_region,
        values='sales',
        names='region',
        title='지역별 매출 비중',
    )
    fig.update_layout(height=400)
    return fig
