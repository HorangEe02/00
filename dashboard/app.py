import streamlit as st
import pandas as pd

from utils.filters import render_sidebar_filters
from utils.charts import (
    create_sales_trend_chart,
    create_product_bar_chart,
    create_region_pie_chart,
)

# ── 페이지 설정 ──
st.set_page_config(
    page_title='Sales Dashboard',
    page_icon='📊',
    layout='wide',
)

# ── 데이터 로딩 (캐싱) ──
@st.cache_data
def load_data():
    df = pd.read_csv('data/sales_data.csv')
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()

# ── 사이드바 필터 ──
df_f = render_sidebar_filters(df)

# ── 헤더 ──
st.title('📊 Sales Analytics Dashboard')
st.markdown('---')

# ── KPI 카드 4개 ──
if len(df_f) > 0:
    total_sales = df_f['sales'].sum()
    total_orders = len(df_f)
    avg_sales = df_f['sales'].mean()

    # 전월 대비 delta 계산
    current_month = df_f['date'].dt.month.max()
    this_month_sales = df_f[df_f['date'].dt.month == current_month]['sales'].sum()
    last_month_sales = df_f[df_f['date'].dt.month == current_month - 1]['sales'].sum()

    if last_month_sales > 0:
        delta_pct = f'{((this_month_sales - last_month_sales) / last_month_sales) * 100:.1f}%'
    else:
        delta_pct = None

    col1, col2, col3, col4 = st.columns(4)
    col1.metric('총 매출', f'₩{total_sales:,.0f}', delta=delta_pct)
    col2.metric('주문 건수', f'{total_orders:,}건')
    col3.metric('평균 주문액', f'₩{avg_sales:,.0f}')
    col4.metric('최다 판매 제품', df_f.groupby('product')['sales'].sum().idxmax())

    st.markdown('---')

    # ── 분석 탭 3개 ──
    tab1, tab2, tab3 = st.tabs(['📈 매출 추이', '📦 제품별 매출', '🗺️ 지역별 매출'])

    with tab1:
        fig = create_sales_trend_chart(df_f)
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        fig = create_product_bar_chart(df_f)
        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        fig = create_region_pie_chart(df_f)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('---')

    # ── CSV 다운로드 버튼 ──
    csv = df_f.to_csv(index=False).encode('utf-8')
    st.download_button(
        '📥 CSV 다운로드',
        data=csv,
        file_name='filtered_sales.csv',
        mime='text/csv',
    )

    # ── 원본 데이터 expander ──
    with st.expander('📋 원본 데이터 보기', expanded=False):
        st.dataframe(df_f, use_container_width=True)

else:
    st.warning('선택한 필터 조건에 해당하는 데이터가 없습니다.')
