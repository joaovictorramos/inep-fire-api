USE [bd_sinape_evoltz]
GO
/****** Object:  Table [dbo].[QUEIMADA]    Script Date: 08/12/2023 11:47:49 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[QUEIMADA](
	[COD_QUEIM] [int] IDENTITY(1,1) NOT NULL,
	[Datahora] [datetime] NOT NULL,
	[Latitude] [float] NOT NULL,
	[Longitude] [float] NOT NULL,
	[Estado] [varchar](2) NOT NULL,
	[Municipio] [varchar](255) NULL,
	[Satelite] [varchar](50) NULL,
 CONSTRAINT [PK_QUEIMADA] PRIMARY KEY CLUSTERED 
(
	[Datahora] ASC,
	[Latitude] ASC,
	[Longitude] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[QUEIMADA_COMPLEMENTO]    Script Date: 08/12/2023 11:47:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[QUEIMADA_COMPLEMENTO](
	[COD_QUEIM] [int] NOT NULL,
	[CAMPO] [varchar](25) NOT NULL,
	[VALOR] [varchar](50) NOT NULL,
 CONSTRAINT [PK__QUEIMADA_COMPLEMENTO] PRIMARY KEY CLUSTERED 
(
	[COD_QUEIM] ASC,
	[CAMPO] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
