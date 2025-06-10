// src/pages/ReportsList.js
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../services/api';
import {
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow,
    Paper,
    CircularProgress,
    Typography,
    Button,
    Chip,
    Box,
} from '@mui/material';

const ReportsList = () => {
    const [reports, setReports] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [pagination, setPagination] = useState({
        count: 0,
        next: null,
        previous: null,
    });
    const navigate = useNavigate();

    useEffect(() => {
        const fetchReports = async () => {
            try {
                const response = await api.get('/reports/');
                setReports(response.data.results);
                setPagination({
                    count: response.data.count,
                    next: response.data.next,
                    previous: response.data.previous,
                });
            } catch (err) {
                setError(err.response?.data?.message || 'Failed to fetch reports');
            } finally {
                setLoading(false);
            }
        };

        fetchReports();
    }, []);

    const handleRowClick = (reportId) => {
        navigate(`/reports/${reportId}`);
    };

    const getStatusColor = (status) => {
        switch (status) {
            case 'pending':
                return 'default';
            case 'reviewed':
                return 'primary';
            case 'dismissed':
                return 'secondary';
            default:
                return 'default';
        }
    };

    if (loading) return <CircularProgress />;
    if (error) return <Typography color="error">{error}</Typography>;

    return (
        <Box sx={{ padding: '20px' }}>
            <Typography variant="h4" gutterBottom>
                Reports Management
            </Typography>
            <Typography variant="subtitle1" gutterBottom>
                Total Reports: {pagination.count}
            </Typography>

            <TableContainer component={Paper}>
                <Table>
                    <TableHead>
                        <TableRow>
                            <TableCell>ID</TableCell>
                            <TableCell>Comment ID</TableCell>
                            <TableCell>Reason</TableCell>
                            <TableCell>Status</TableCell>
                            <TableCell>Reviewed</TableCell>
                            <TableCell>Created At</TableCell>
                            <TableCell>Actions</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {reports.map((report) => (
                            <TableRow key={report.id} hover>
                                <TableCell>{report.id}</TableCell>
                                <TableCell>{report.comment}</TableCell>
                                <TableCell>{report.reason}</TableCell>
                                <TableCell>
                                    <Chip
                                        onClick= {() => {}}
                                        label={report.status}
                                        color={getStatusColor(report.status)}
                                    />
                                </TableCell>
                                <TableCell>
                                    {report.is_reviewed ? 'Yes' : 'No'}
                                </TableCell>
                                <TableCell>
                                    {new Date(report.created_at).toLocaleString()}
                                </TableCell>
                                <TableCell>
                                    <Button
                                        variant="outlined"
                                        onClick={() => handleRowClick(report.id)}
                                    >
                                        View Details
                                    </Button>
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>

            {/* Pagination can be added here if needed */}
            {pagination.count === 0 && (
                <Typography variant="body1" sx={{ mt: 2 }}>
                    No reports found.
                </Typography>
            )}
        </Box>
    );
};

export default ReportsList;