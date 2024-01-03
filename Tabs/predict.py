import streamlit as st

from web_function import predict

def app(df, x, y):
    st. title("halaman prediksi")
    
    col1,col2,col3, = st.columns(3)
   
    with col1:
        bp = st.text_input('input nilai bp')
    with col1:
        sg = st.text_input('input nilai sg')
    with col1:
        al = st.text_input('input nilai al')
    with col1:
        su	= st.text_input('input nilai su')
    with col1:
        rbc= st.text_input('input nilai rbc')
    with col1:
        pc= st.text_input('input nilai pc')
    with col1:
        pcc= st.text_input('input nilai pcc')
    with col1:
        ba	= st.text_input('input nilai ba')
    with col2:
        bgr	= st.text_input('input nilai bgr')
    with col2:
        bu	= st.text_input('input nilai bu')
    with col2:
        sc= st.text_input('input nilai sc')
    with col2:
        sod	= st.text_input('input nilai sod')
    with col2:
        pot= st.text_input('input nilai pot')
    with col2:
        hemo= st.text_input('input nilai home')
    with col2:
        pcv= st.text_input('input nilai pcv')
    with col2:
        wc	= st.text_input('input nilai wc')
    with col2:
        rc	= st.text_input('input nilai rc')
    with col3:
        htn= st.text_input('input nilai htn')
    with col3:
        dm	= st.text_input('input nilai dm')
    with col3:
        cad	= st.text_input('input nilai cad')
    with col3:
        appet= st.text_input('input nilai appet')
    with col3:
        pe	= st.text_input('input nilai pe')
    with col3:
        ane= st.text_input('input nilai ane')

    features = [bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wc,rc,htn,dm,cad,appet,pe,ane,]

    #Tombol perdiksi
    if st.button("prediksi"):
        prediction, score = predict(x,y, features)
        score = score
        st.info ("prediksi sukses....")

        if (prediction == 1):
            st.warning("Orang tersebut rentan terkena penyakit ginjaol")
        else:
            st.success("orang tersebut relatif aman dari penyakit ginjal")

        st. write("modal yang digunakan memiliki tingkat akurasi", (score*100),"%")