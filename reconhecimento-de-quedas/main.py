from cvzone.PoseModule import PoseDetector
import cv2
import cvzone

def main():
    detector = PoseDetector()
    captura_de_video = cv2.VideoCapture(0) # 0 para webcam padrão
   
    captura_de_video.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
    captura_de_video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    diferenca = 1
    if not captura_de_video.isOpened():
        raise Exception("Não foi possível abrir a webcam.")       
    try:
        while True:
            ret, quadro = captura_de_video.read()
            if not ret:
                break                    
            resultado = detector.findPose(quadro)
            pontos,bbox = detector.findPosition(quadro,draw=False)            
            if diferenca <=0:                
                cv2.putText(quadro,'QUEDA',(50,50),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)     
            cv2.imshow('Reconhecimento de Faces', quadro)           
            if len(pontos)>=1:                
                cabeca = pontos[0][1]
                joelho = pontos[25][1]
                #print(joelho, cabeca)
                diferenca = joelho-cabeca     
                #print(diferenca)                                  
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        captura_de_video.release()
        cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
