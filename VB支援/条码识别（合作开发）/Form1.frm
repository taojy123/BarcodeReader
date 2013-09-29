VERSION 5.00
Begin VB.Form Form1 
   BorderStyle     =   1  'Fixed Single
   Caption         =   "条码识别_插件版"
   ClientHeight    =   3555
   ClientLeft      =   45
   ClientTop       =   435
   ClientWidth     =   4425
   Icon            =   "Form1.frx":0000
   LinkTopic       =   "Form1"
   MaxButton       =   0   'False
   ScaleHeight     =   3555
   ScaleWidth      =   4425
   StartUpPosition =   3  '窗口缺省
   Begin VB.Timer Timer2 
      Enabled         =   0   'False
      Interval        =   10000
      Left            =   2760
      Top             =   2280
   End
   Begin VB.Timer Timer1 
      Enabled         =   0   'False
      Interval        =   500
      Left            =   2160
      Top             =   2280
   End
   Begin VB.PictureBox Picture1 
      AutoRedraw      =   -1  'True
      AutoSize        =   -1  'True
      Height          =   1695
      Left            =   1680
      ScaleHeight     =   1635
      ScaleWidth      =   2355
      TabIndex        =   1
      Top             =   360
      Visible         =   0   'False
      Width           =   2415
   End
   Begin VB.CommandButton Command1 
      Caption         =   "开始识别"
      Enabled         =   0   'False
      Height          =   375
      Left            =   240
      TabIndex        =   0
      Top             =   2880
      Width           =   2175
   End
   Begin VB.Label Label5 
      AutoSize        =   -1  'True
      Caption         =   "识 别 率："
      Height          =   180
      Left            =   360
      TabIndex        =   6
      Top             =   2160
      Width           =   900
   End
   Begin VB.Label Label4 
      AutoSize        =   -1  'True
      Caption         =   "未能识别："
      Height          =   180
      Left            =   360
      TabIndex        =   5
      Top             =   1680
      Width           =   900
   End
   Begin VB.Label Label3 
      AutoSize        =   -1  'True
      Caption         =   "识 别 出："
      Height          =   180
      Left            =   360
      TabIndex        =   4
      Top             =   1200
      Width           =   900
   End
   Begin VB.Label Label2 
      AutoSize        =   -1  'True
      Caption         =   "剩    余："
      Height          =   180
      Left            =   360
      TabIndex        =   3
      Top             =   720
      Width           =   900
   End
   Begin VB.Label Label1 
      AutoSize        =   -1  'True
      Caption         =   "发现图片："
      Height          =   180
      Left            =   360
      TabIndex        =   2
      Top             =   240
      Width           =   900
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit


Private Sub Command1_Click()
    lRE = lFileNum
    Timer1.Enabled = True
    
    Command1.Caption = "正在识别.."
    Command1.Enabled = False
    
    'Form1.Cls
End Sub

Private Sub Form_Load()

    Call BC_Init
    
    If Command <> "" Then
        Dim sPos As String, Pos() As String, sBarCode As String
        
        Timer2.Enabled = True
        
        
        Picture1.Picture = LoadPicture("C:\ReaderPlugin\t.jpg")
    
        sPos = GetPos
        If sPos <> "" Then
            Pos = Split(sPos, ",")
            
            'Form1.Print Pos(0) & "," & Pos(1)
            
            sBarCode = ScanBar(Pos(0) - 5, Pos(1) + 5)
            
            Open "C:\ReaderPlugin\Result.txt" For Output As #1
            
            If sBarCode <> "" Then
                Print #1, sBarCode
            Else
                Print #1, "unread"
            End If
            
            Close #1
            
            End
        End If
        
    Else
        
        Call EnumFiles(App.Path)
    
        Label1.Caption = Label1.Caption & lFileNum & " 张"
    
        If lFileNum > 0 Then
            Command1.Enabled = True
        End If
        
    End If
    
End Sub


Private Sub Timer1_Timer()
    Dim sPos As String, Pos() As String, sBarCode As String
    
    Timer1.Enabled = False
    
    Picture1.Picture = LoadPicture(sFile(lpFile))

    sPos = GetPos
    If sPos <> "" Then
        Pos = Split(sPos, ",")
        
        'Form1.Print Pos(0) & "," & Pos(1)
        
        sBarCode = ScanBar(Pos(0) - 5, Pos(1) + 5)
        
        If sBarCode <> "" Then
            Call ReNameFile(sBarCode)
            
            Call ShowRes(True)
        Else
            Call ShowRes(False)
        End If
    Else
        lRE = lRE - 1
        If lRE > 0 Then
            Timer1.Enabled = True
        Else
            Command1.Caption = "识别完成"
            MsgBox "识别完成！"
        End If
    End If
End Sub


Private Sub ShowRes(ByVal bParam As Boolean)
    lRE = lRE - 1
    lpFile = lpFile + 1
    
    If bParam = True Then
        lOK = lOK + 1
    Else
        lNO = lNO + 1
    End If

    Label2.Caption = "剩    余：" & lRE & " 张"
    Label3.Caption = "识 别 出：" & lOK & " 张"
    Label4.Caption = "未能识别：" & lNO & " 张"
    Label5.Caption = "识 别 率：" & FormatNumber(lOK / (lOK + lNO), 2) * 100 & "%"
    
    If lRE > 0 Then
        Timer1.Enabled = True
    Else
        Command1.Caption = "识别完成"
        MsgBox "识别完成！"
    End If
End Sub


Private Function GetPos() As String
    On Error Resume Next
    Dim xI As Long, yI As Long, i As Long, isFind As Boolean
    
    For xI = Picture1.Width / 45 To Picture1.Width / 15
        For yI = 0 To 85
            If InColor(xI, yI, 30, 30, 30, 30) = True Then
                isFind = True
                For i = 1 To 15
                    If InColor(xI, yI + i, 30, 30, 30, 30) = False Then
                        isFind = False
                        Exit For
                    End If
                Next
            
                If isFind = True Then
                    GetPos = xI & "," & yI
                    Exit Function
                End If
            End If
        Next
    Next
End Function


Private Sub ReNameFile(ByVal sParam As String)
    Dim i As Long, fName As String
    
    fName = sParam
    
    Do Until Dir(fName & ".jpg") = ""
        i = i + 1
        fName = sParam & "(" & i & ")"
    Loop
    
    Name sFile(lpFile) As fName & ".jpg"
End Sub




Private Sub Timer2_Timer()
Timer2.Enabled = False
End
End Sub
