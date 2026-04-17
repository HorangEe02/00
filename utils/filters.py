import streamlit as st
import pandas as pd


def render_sidebar_filters(df: pd.DataFrame) -> pd.DataFrame:
    """사이드바 필터를 렌더링하고 필터링된 DataFrame을 반환"""
    with st.sidebar:
        st.title('🔍 필터')

        # 날짜 범위 선택
        min_date = df['date'].min().date()
        max_date = df['date'].max().date()

        date_range = st.date_input(
            '기간 선택',
            value=[min_date, max_date],
            min_value=min_date,
            max_value=max_date,
        )

        # 지역 선택
        all_regions = sorted(df['region'].unique())
        selected_regions = st.multiselect(
            '지역 선택',
            options=all_regions,
            default=all_regions,
        )

        # 제품 선택
        all_products = sorted(df['product'].unique())
        selected_products = st.multiselect(
            '제품 선택',
            options=all_products,
            default=all_products,
        )

    # 필터 적용
    mask = pd.Series([True] * len(df), index=df.index)

    if selected_regions:
        mask &= df['region'].isin(selected_regions)
    else:
        mask &= False

    if selected_products:
        mask &= df['product'].isin(selected_products)
    else:
        mask &= False

    if len(date_range) == 2:
        start, end = date_range
        mask &= (df['date'] >= pd.Timestamp(start))
        mask &= (df['date'] <= pd.Timestamp(end))

    return df[mask]
