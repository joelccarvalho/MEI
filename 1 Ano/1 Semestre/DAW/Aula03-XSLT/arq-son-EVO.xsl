<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    version="2.0">
    
    <xsl:output method="html" encoding="UTF-8" indent="yes"/>
    
    <xsl:template match="/">
        <html>
            <head>
                <title>Arquivo Sonoro EVO</title>
            </head>
            <body>
                <!--<ol>
                    <xsl:apply-templates select="//doc"> <!-\- atravessa todos os docs -\->
                        <xsl:sort select="tit"></xsl:sort>
                    </xsl:apply-templates>
                </ol>-->
                <h2>Arquivo Sonoro EVO</h2>
                <table border="1" width="100%">
                    <tr>
                        <td width="30%" valign="top">
                            <h3>Índice de Músicas</h3>
                            <ol>
                                <xsl:apply-templates select="//doc" mode="indice"> <!-- aponta para o indice lá em baixo -->
                                    <xsl:sort select="tit"/>
                                </xsl:apply-templates>
                            </ol>
                        </td>
                        <td>
                            <xsl:apply-templates/>
                        </td>
                    </tr>
                </table>
            </body>
        </html>
    </xsl:template>
    
    <!-- Template para índice -->
    
    <xsl:template match="doc" mode="indice">
        <li>
            <a name="i{generate-id()}"/>
            <a href="#{generate-id()}"> <!-- Gera um id para apontar -->
                <xsl:value-of select="tit"/>
            </a>
        </li>
    </xsl:template>
    
    <!-- Template para conteúdo -->
    
    <xsl:template match="doc">
        <a name="{generate-id()}"/> <!-- Gera um id para apontar, ambas em sintonia -->
        <p><b>Título: </b> <xsl:value-of select="tit"/></p>
        <p><b>Província: </b> <xsl:value-of select="prov"/></p>
        <p><b>Local: </b> <xsl:value-of select="local"/></p>
        <p><b>Instrumento: </b> <xsl:value-of select="inst"/></p>
        <p><b>Duração: </b> <xsl:value-of select="duracao"/></p>
        <address>
            [<a href="#i{generate-id()}">Voltar ao índice</a>]
        </address>
        <center><hr width="80%"/></center>
    </xsl:template>
</xsl:stylesheet>