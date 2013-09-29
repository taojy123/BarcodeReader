Attribute VB_Name = "Module1"
Option Explicit


Public Declare Function GetPixel Lib "gdi32" (ByVal hDC As Long, ByVal x As Long, ByVal y As Long) As Long


'�ѳ�������ɫת������"R,G,B"���ַ�����
Public Function GetRGB(ByVal lColor As Long) As String
    Dim sRed As String, sGreen As String, sBlue As String

    sRed = lColor Mod 256
    sGreen = Int(lColor / 256) Mod 256
    sBlue = Int(lColor / 256 / 256)
    
    GetRGB = sRed & "," & sGreen & "," & sBlue
End Function

'һ��RGB��ɫ�ķ������ڲ���һ����Χ��,picClr�Ǵ�ͼ�ϵõ�����ɫ��srcClr����ɫ��׼��pDecl������ƫ�Χ
Public Function IsRGB(ByVal picClr As String, ByVal srcClr As String, ByVal pDecl As Long) As Boolean
    Dim i As Long, picRGB() As String, srcRGB() As String, uRGB(2, 1) As Long, sRGB() As String
    
    picRGB = Split(picClr, ",")
    srcRGB = Split(srcClr, ",")
    
    For i = 0 To 2
        If InStr(srcRGB(i), ":") = 0 Then
            uRGB(i, 0) = srcRGB(i) - pDecl
            uRGB(i, 1) = srcRGB(i) + pDecl
        Else
            sRGB = Split(srcRGB(i), ":")
            uRGB(i, 0) = sRGB(0)
            uRGB(i, 1) = sRGB(1)
        End If
        If CLng(picRGB(i)) < uRGB(i, 0) Or CLng(picRGB(i)) > uRGB(i, 1) Then
            Exit Function
        End If
    Next
    
    IsRGB = True
End Function


'�õ�RGB��ɫ���ַ���
Public Function GetColor(ByVal x As Long, ByVal y As Long) As String
    GetColor = GetRGB(GetPixel(Form1.Picture1.hDC, x, y)) 'API GetPixel��Picture��Point��������һЩ
End Function


'�ж�ĳ����ɫ�ǲ�����ָ������ɫ��Χ��
Public Function InColor(ByVal x As Long, ByVal y As Long, ByVal R As String, ByVal G As String, ByVal B As String, ByVal pDecl As Long) As Boolean
    InColor = IsRGB(GetColor(x, y), R & "," & G & "," & B, pDecl)
End Function
