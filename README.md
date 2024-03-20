# ai_python
인공지능 코딩을 위한 실용 파이썬

1. 기본 환경 설정
   
    1.2. 개발 환경 구축 (ml_env)

    conda list

    conda create -n ml_env python=3.11

    conda env list

    conda env remove -n ml_env

    conda activate ml_env

    conda deactivate

    conda --version

    python --version

    exit



    1.2. tensorflow 설치
    
    - 설치 :: pip install tensorflow-cpu
    
    - 작동확인
   
    python
    
    import tensorflow as tf
   
    print(tf.__version__)
   
    tf.print(tf.__version__)
   

    hello = tf.constant("Hello Tensorflow")
   
    print(hello)
   
    tf.print(hello)
   

    quit()
   
    
    - 핵심 라이브러리 설치 :: conda install pandas matplotlib seaborn scikit-learn
   
    
    1.3. 파이썬 코딩 기초 개념
    
    - Standard Library
    - NumPy : Numerical Python
    - Pandas : Panel Data
    - Matplotlib / Seaborn : Visualization

    --- Scikit-learn, TensorFlow For AI
